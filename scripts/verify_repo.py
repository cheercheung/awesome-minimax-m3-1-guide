#!/usr/bin/env python3
"""Portable verification of complete handbook, case, media, Prompt and locale parity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,json,csv,hashlib,argparse,sys
ROOT=Path(__file__).resolve().parents[1];LOCALES=['en','es','pt','ja','ko','de','fr','tr','zh-TW','zh-CN','ru'];PREFIX={'en':'Case','es':'Caso','pt':'Caso','ja':'ケース','ko':'사례','de':'Fall','fr':'Cas','tr':'Örnek','zh-TW':'案例','zh-CN':'案例','ru':'Пример'};GUIDES=['task-selection','reasoning','multimodal','context-cache','workflows','migration','protocols'];errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def fenced(s):
 lines=s.splitlines(keepends=True);out=[];clean=[];marker=None;code=[]
 for l in lines:
  if marker:
   if re.fullmatch(re.escape(marker)+r'\s*',l.rstrip('\r\n')):
    t=''.join(code);out.append(t[:-1] if t.endswith('\n') else t);marker=None;code=[];clean.append('\n')
   else:code.append(l)
  else:
   m=re.match(r'^(`{3,}|~{3,})\w*\s*$',l.rstrip('\r\n'))
   if m:marker=m[1];code=[]
   else:clean.append(l)
 check(marker is None,'unclosed code fence');return out,''.join(clean)
class Images(HTMLParser):
 def __init__(self):super().__init__();self.href='';self.images=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='a':self.href=a.get('href','')
  if t=='img':self.images.append({**a,'link':self.href})
 def handle_endtag(self,t):
  if t=='a':self.href=''
def image_list(s):p=Images();p.feed(fenced(s)[1]);return p.images
def anchors(s):
 s=fenced(s)[1];a=set(re.findall(r'<a id="([^"]+)"',s))
 for h in re.findall(r'^#{1,6} (.+)',s,re.M):a.add(re.sub(r'[^\w\- ]','',h.lower(),flags=re.U).replace(' ','-'))
 return a
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--english-only',action='store_true');args=ap.parse_args();data=json.loads((ROOT/'data/use-cases.json').read_text());cases=data['items'];cfg=json.loads((ROOT/'data/usecase-update-config.json').read_text());source=json.loads((ROOT/'sources/handbook-extract.json').read_text());raw={x['id']:x for x in source['cases']};check(len(cases)==len(raw)==53,'case/source denominator');check([x['public_number'] for x in cases]==list(range(1,54)),'stable numbering/order');check(sum(c['expected_public_visual_count'] for c in cases)==data['expected_public_visual_count']==53,'visual denominator');check(sum(bool(c['prompts']) for c in cases)==31,'Prompt case count');check(len({c['source_url'] for c in cases})==53,'unique sources')
 for c in cases:
  check(sha(raw[c['group_id']]['raw_source_row'])==c['raw_source_row_sha256']==raw[c['group_id']]['raw_sha256'],c['group_id']+' source hash')
  for p in c['prompts']:
   check(sha(p['text'])==p['sha256'],p['id']+' text hash');path=ROOT/'prompts'/(c['group_id']+'.md');check(path.is_file(),p['id']+' file');actual=fenced(path.read_text())[0];check(actual==[p['text']],p['id']+' complete text')
   if p['source_format']=='attachment-original':check((ROOT/'sources/flowdesk-PROMPT.txt').read_text()==p['text'],p['id']+' original input')
   else:
    row=raw[c['group_id']]['raw_source_row'];cell=raw[c['group_id']]['query_source_cell'];check(cell in row,p['id']+' source cell');start=cell.index('```');first=cell.index('<br>',start);last=cell.rfind('```');expected=cell[first+4:last].replace('<br>','\n').removesuffix('\n');check(expected==p['text'],p['id']+' source span')
  check(c['source_media_count']==c['expected_public_visual_count']==len(c['r2_media_items'])==len(c['source_media_urls']),c['group_id']+' media count')
 with (ROOT/'data/use-cases.csv').open(newline='') as f:rows=list(csv.DictReader(f))
 check(len(rows)==53,'CSV denominator')
 for row,c in zip(rows,cases):
  for k in ['public_number','group_id','category','type','title','takeaway','source_url','author_handle','attribution_role','date','date_basis','demo_url','playable_video_url']:check(row[k]==('' if c.get(k) is None else str(c[k])),'CSV '+c['group_id']+' '+k)
  check(row['prompt_count']==str(len(c['prompts'])),'CSV Prompt count');check(row['source_media_count']==str(c['source_media_count']),'CSV media count')
 display_categories=[x.removeprefix('category-') for x in cfg['namespace']['category_anchors']];display_cases=sorted(cases,key=lambda c:(display_categories.index(c['category']),c['public_number']));translations={};guide_counts={};english_titles={c['public_number']:c['title'] for c in cases};locale_list=['en'] if args.english_only else LOCALES
 if not args.english_only:check({p.name for p in ROOT.glob('README*.md')}=={'README.md' if l=='en' else f'README_{l}.md' for l in LOCALES},'README locale set')
 for lang in locale_list:
  path=ROOT/('README.md' if lang=='en' else f'README_{lang}.md');text=path.read_text();clean=fenced(text)[1];matches=list(re.finditer(r'<a id="case-(\d+)"></a>\n### ([^\n]+)',clean));check([int(m[1]) for m in matches]==[c['public_number'] for c in display_cases],lang+' case identities');check('width="760"' in clean and 'images/banner.svg' in clean,lang+' banner');check(not re.search(r'^Type:|^## .*Introduction|^## .*Quick Start',clean,re.M),lang+' owner profile');check(len(re.findall(r'\]\(#category-',clean))==11,lang+' categories');local_titles=[];check(fenced(text)[0]==[p['text'] for c in display_cases for p in c['prompts'] if len(p['text'])<=1000],lang+' immutable inline Prompt text')
  for i,(m,c) in enumerate(zip(matches,display_cases)):
   end=matches[i+1].start() if i+1<len(matches) else clean.index('## 📖',m.end());body=clean[m.end():end];head=m[2];title=re.match(re.escape(PREFIX[lang])+r' (\d+): \[([^\]]+)\]\(([^)]+)\)',head);check(bool(title),lang+' heading '+str(i+1))
   if title:
    check(int(title[1])==c['public_number'] and title[3]==c['source_url'],lang+' source '+str(i+1));local_titles.append(title[2]);check(title[2]==c['title'] if lang=='en' else title[2]!=c['title'],lang+' title translation '+str(i+1))
   bold=re.search(r'^\*\*(.+)\*\*$',body,re.M);check(bool(bold),lang+' takeaway '+str(i+1));check(bold[1]==c['takeaway'] if lang=='en' and bold else bool(bold) and bold[1]!=c['takeaway'],lang+' takeaway translation '+str(i+1))
   ims=image_list(body);expected=c['r2_media_items'];check(len(ims)==len(expected),lang+' visuals '+str(i+1))
   for im,item in zip(ims,expected):
    url=item['poster_url'] if item['kind']=='video' else item['image_url'];target=item['playable_video_url'] if item['kind']=='video' else item['image_url'];check(im.get('src')==url and im.get('link')==target and im.get('height')==str(cfg['presentation'].get('paired_image_height',280) if len(expected)==2 else cfg['presentation']['case_image_height']) and not im.get('width'),lang+' complete media '+str(i+1));check(title is not None and im.get('alt')==title[2],lang+' alt '+str(i+1))
   if len(expected)==2:
    tables=re.findall(r'<table>(.*?)</table>',body,re.S)
    check(len(tables)==1 and len(re.findall(r'<tr\b',tables[0]))==1 and len(re.findall(r'<td\b',tables[0]))==2,lang+' two-column pair '+c['group_id'])
   if c['prompts'] and len(c['prompts'][0]['text'])>1000:check('prompts/'+c['group_id']+'.md' in body,lang+' long Prompt link '+str(i+1))
   if c['display_date']:check(c['date'] in body,lang+' PR date '+str(i+1))
  nav=re.findall(r'\]\(#category-([^)]+)\)\s*\|\s*(\d+)',clean)
  category_order=display_categories
  check(nav==[(cat,str(sum(c['category']==cat for c in cases))) for cat in category_order],lang+' category counts')
  for ci,cat in enumerate(category_order):
   start=clean.index('<a id="category-'+cat+'"></a>');end=clean.index('<a id="category-'+category_order[ci+1]+'"></a>') if ci+1<len(category_order) else clean.index('## 📖',start)
   observed=[int(x) for x in re.findall(r'<a id="case-(\d+)"></a>',clean[start:end])]
   check(observed==[c['public_number'] for c in cases if c['category']==cat],lang+' category membership '+cat)
  translations[lang]=local_titles
  paths=list((ROOT/'docs/guide'/lang).glob('*.md'));check({p.stem for p in paths}==set(GUIDES),lang+' seven guides');guide_counts[lang]=len(paths)
  for gp in paths:
   s=gp.read_text();check(len(s)>300 and '../../../'+path.name in s,lang+' Guide content/navigation');check(not re.search('TODO|translation pending|translate to',s,re.I),lang+' Guide placeholder')
 if not args.english_only:
  for lang,titles in translations.items():
   for other,other_titles in translations.items():
    if lang!=other:check(titles!=other_titles,'identical locale title sequences '+lang+'/'+other)
 files=[p for p in ROOT.rglob('*.md') if not {'.git','.codex','assets'}&set(p.relative_to(ROOT).parts)]
 for p in files:
  _,s=fenced(p.read_text());width=None
  for line in s.splitlines():
   if line.startswith('|'):
    cols=len(re.split(r'(?<!\\)\|',line))-2
    if width is None:width=cols
    check(cols==width,str(p.relative_to(ROOT))+' table columns')
   else:width=None
  for target in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)',s):
   u=urlsplit(target)
   if u.scheme:continue
   dest=p.parent/unquote(u.path) if u.path else p
   if args.english_only and re.match(r'README_.+\.md$',dest.name) and not dest.exists():continue
   check(dest.is_file(),str(p.relative_to(ROOT))+' missing '+target)
   if dest.is_file() and u.fragment and dest.suffix=='.md':check(unquote(u.fragment) in anchors(dest.read_text()),str(p.relative_to(ROOT))+' fragment '+target)
  check(not re.search(r'<video\b',s,re.I),str(p.relative_to(ROOT))+' raw video embed')
 public_paths=[p for p in ROOT.rglob('*') if p.is_file() and not {'.git','.codex','assets'}&set(p.relative_to(ROOT).parts)]
 for p in public_paths:
  check(p.name not in ['.DS_Store'] and p.suffix not in ['.pyc'],str(p)+' system file')
  if p.suffix in ['.md','.json','.csv','.py','.yml','.txt']:check(('/Users/'+'cheercheung/') not in p.read_text(),str(p.relative_to(ROOT))+' local machine path')
 if errors:print('FAIL\n'+'\n'.join(errors));return 1
 print('PASS: 53 cases; 53 complete visuals; 31 source-verified Prompts; '+str(len(locale_list))+' README languages; '+str(sum(guide_counts.values()))+' Guide pages; CSV, source rows and relative links');return 0
if __name__=='__main__':sys.exit(main())

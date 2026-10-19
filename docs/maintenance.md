# Maintenance

## Source of truth

`data/use-cases.json` contains the 53 curated cases. `data/use-cases.csv` and `data/use-cases.md` are derived from it. Stable case numbers follow the supplied handbook; grouping follows the eleven task categories. `sources/handbook-extract.json` retains the original exported source rows and hashes. Exact Prompt files live in `prompts/`; the Flowdesk input also has its original text snapshot.

## Case format

Use a stable `case-N` anchor, linked case heading, concise bold takeaway, centered source visuals and optional supplied Prompt. Images use height 280 without a fixed width. Video posters link to browser-compatible MP4s; GIFs remain animated. Complete source attachment sets and their input/output roles stay in data. Public source attribution follows the supplied handbook; public PR authors are named when known. Intake dates are recorded as intake dates in data and are not presented as creation dates.

Do not add Introduction, Quick Start, type labels, promotional calls to action, collection-scope paragraphs or repetitive audit notes to cases. Keep internal evidence notes in the dataset and maintenance records. A task summary must not become an invented original Prompt. Long supplied Prompts link to their complete files.

## Update checklist

1. Preserve source material and review every candidate against a concrete task and corresponding output
2. Fix case identity, category, attribution, date basis, Prompt boundary and full attachment set before rendering
3. Freeze source hashes and the expected visual set; verify source fidelity before README changes
4. Prepare complete browser media with original hashes and explicit transformations, upload under this repository namespace and verify origin bytes
5. Update English first, run its gate, then synchronize the other ten READMEs and all seven Guide modules in each language
6. Refresh CSV and index; compare original Prompt text and source row hashes
7. Run portable checks, full links, rendered media and semantic localization checks
8. Commit, push and read back the exact commit, repository metadata, READMEs and media before reporting publication

## Validation

```bash
python3 scripts/verify_repo.py --english-only
python3 scripts/verify_repo.py
git diff --check
```

The portable check uses committed files and the declared public URLs; local collector paths and ignored media are not dependencies. Network availability, GitHub rendering and real model execution require separate evidence. No paid API test or model generation is part of editing this source-backed collection.

## Known source corrections

The chemistry example is IChO 2009, not IPHO. The rubber report concerns rubber-to-tire transmission. Nine explanatory cells in its workbook were converted from invalid formula expressions to literal text; numeric calculation cells were preserved. The rubber HTML includes its chart dependency for offline viewing. Tool-assisted video workflows retain their model/tool roles. The current Guide model ID is MiniMax-M3.1-Flash; original Preview strings stay intact in source Prompts.

Star History remains absent below ten live stars; when eligible it belongs at the end of each README

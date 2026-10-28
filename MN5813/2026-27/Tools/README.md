# Tools

*`check.py` tests your work before you submit it. `bundle.py` packs it for upload. The two fetch scripts download the assessment datasets.*


## fetch_lfb.py and fetch_abcd.py

Each script fetches its dataset once into your `work/data/` folder (`work/data/lfb/` and `work/data/abcd/`), with a manifest of what it wrote. A later run with `--check` confirms that your tables still match the manifest:

```bash
python3 Tools/fetch_lfb.py     # group project: London Fire Brigade incidents and mobilisations
python3 Tools/fetch_abcd.py    # individual report: The abcd project record at a pinned release
python3 Tools/fetch_lfb.py --check   # do my tables match my manifest?
```

The data notes explain what each script writes and what the data means: [lfb-data.md](../Assessment/lfb-data.md) and [abcd-record.md](../Assessment/abcd-record.md).


## check.py

`check.py` runs the same Tier-1 checks I run, to make sure your work runs.

```bash
python3 Tools/check.py        # check the current folder
python3 Tools/check.py path/to/work
```

The `--resolve-dois` option is off by default. It asks Crossref whether the DOIs in your notebook's Markdown cells resolve. A run with `--resolve-dois` writes the results into `precheck-report.json`.

Important: Do not edit `check.py` directly.


## bundle.py

`bundle.py` packs your notebook and the shared files it needs into one zip file, ready for upload to Moodle.

```bash
python3 Tools/bundle.py --lc final --week 12 --id P401001 [path]
```

**It bundles your [Prompt Diary](../Guides/glossary.md#term-prompt-diary) and leaves the rest of your record out, deliberately.**

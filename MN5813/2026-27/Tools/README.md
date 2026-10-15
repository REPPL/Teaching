# Tools

*`check.py` tests your work before you submit it. `bundle.py` packs it for upload. The two fetch scripts download the assessment datasets.*


## fetch_lfb.py and fetch_abcd.py

This repository points to the two assessment datasets rather than storing copies. Each script fetches its dataset once into your `work/data/` folder (`work/data/lfb/` and `work/data/abcd/`), with a manifest of what it wrote. git ignores the LFB data there, but not the abcd tables. If an older version of a script wrote into `Tools/data/`, the next run moves that copy into `work/data/`, so you do not download it again. A later run with `--check` confirms that your tables still match the manifest:

```bash
python3 Tools/fetch_lfb.py     # group project: London Fire Brigade incidents and mobilisations
python3 Tools/fetch_abcd.py    # individual report: The abcd project record at a pinned release
python3 Tools/fetch_lfb.py --check   # do my tables match my manifest?
```

Both scripts need the module's Python environment, which your Codespace has. They need network access on the first run only, to download the data. The data notes explain what each script writes and what the data means: [lfb-data.md](../Assessment/lfb-data.md) and [abcd-record.md](../Assessment/abcd-record.md).


## check.py

You need to know what `check.py` does, not how it works. It is a self-check that needs only Python 3.11 or later, with nothing else to install. It runs the same Tier-1 checks I run, to make sure your work runs.

```bash
python3 Tools/check.py        # check the current folder
python3 Tools/check.py path/to/work
```

The `--resolve-dois` option is off by default. It asks Crossref (api.crossref.org) whether the DOIs in your notebook's Markdown cells resolve. It is the only part of this tool that uses the network. `--offline-safe` forces it off. A run with `--resolve-dois` writes the results into `precheck-report.json`.

Important: Do not edit `check.py` directly. It is generated. Its header names its source.


## bundle.py

`bundle.py` packs your notebook and the shared files it needs into one zip file, ready for upload to Moodle. Like `check.py`, it needs only Python 3.11 or later. The zip also contains `manifest.json`, which records the file list, the sha256 checksums, the week, your group or candidate ID, and the tool versions.

```bash
python3 Tools/bundle.py --lc final --id P401001 [path]
```

(The tool also supports `--portfolio`, `--excerpts`, and `--aias` for module set-ups that use them; <!-- gen:values.yml#module.code -->MN5813<!-- /gen --> <!-- gen:values.yml#module.year -->2026-27<!-- /gen --> does not.)

**It leaves your record out, deliberately.** `transcripts/`, `.specstory/`, `standup.md`, and `retro.md` are never bundled. They are yours, and nothing here sends them anywhere by mistake. This tool never runs your notebook and never uses the network.

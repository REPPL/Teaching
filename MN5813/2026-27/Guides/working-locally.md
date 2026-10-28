# Working locally (optional)

*Optional, for your own time.*

> ⚠️ **Draft:** This page is a draft. It will be confirmed at a later date.

> **From:** A. Partner, [Runnymede Analytics](./glossary.md#term-runnymede-analytics)
> **To:** You (Junior [Analyst](./glossary.md#term-analyst))
> **Re:** If you would rather work from your own desk
>
> The firm's workstation is the Codespace. A local copy is a convenience on top of it, not a replacement.


## Why you might want this

- **Offline work.** A Codespace needs an internet connection. Your own machine does not
- **Personal preference.** You already have VS Code set up the way you like it
- **Codespaces hours.** You get a limited number of free Codespaces hours each month. Local work costs nothing


## What you need

Install the following:

1. **VS Code.** Download it from [code.visualstudio.com](https://code.visualstudio.com/), run the installer, and keep every option as it is
2. **Python 3.12 or newer.** Download it from [python.org/downloads](https://www.python.org/downloads/). On Windows, tick **"Add python.exe to PATH"** on the installer's first screen.

   Then check that Python is installed. Open VS Code's terminal with **Terminal → New Terminal** or `` Ctrl+` ``. Run `python --version`, or `python3 --version` on macOS. It prints the version number

3. **Git.** Download it from [git-scm.com/downloads](https://git-scm.com/downloads). On Windows, run the Git for Windows installer and keep every option as it is. On macOS, run `git --version` in VS Code's terminal. If git is missing, macOS offers to install its Command Line Tools. Accept, and wait for that to finish.

   Then check that git is installed. Run `git --version` in VS Code's terminal. It prints the version number

4. **GitHub Copilot and Copilot Chat.** Open VS Code's Extensions view (`Ctrl/Cmd+Shift+X`), search for each name, and install the one published by GitHub. Sign in with the same GitHub account you use for your Codespace
5. **Python and Jupyter extensions.** In the same Extensions view, install **Python** and **Jupyter**, both published by Microsoft
6. **[SpecStory](./glossary.md#term-specstory)** *(optional)*. Search the Extensions view for "SpecStory" and install it if you want your AI sessions recorded automatically. The module requires your **[AI Use Record](./glossary.md#term-ai-use-record)** (see the [AI guide](./ai-guide.md)). SpecStory is one way to keep it, not the only way


## Get your project onto your machine

Your Codespace opens your own GitHub repository, the one you made in [Your workstation, Step 2](./codespaces-start.md#step-2-create-your-own-repository). Copy it to your own machine with git. In VS Code's terminal, run:

```
git clone <your repository's URL>
```

To find the URL, open your repository on GitHub and click the green **`< > Code`** button. Copy the URL from the **Local** tab, next to the **Codespaces** tab. Then open the new folder in VS Code with **File → Open Folder…**.

Then give the new folder the git setting your Codespace has. In VS Code's terminal, inside the new folder, run:

```
git config pull.rebase false
```

New materials reach your repository on GitHub through Get new materials, as in [Step 3a](./codespaces-start.md#step-3a-get-new-materials) of the Your workstation guide. To bring them to your machine, run `git pull --no-edit`.

Your Codespace and your local copy are two separate copies of the same repository. Run `git pull --no-edit` before you start. Run `git push` when you finish. Work in either, as long as you push before switching.


## Install the module's packages

Your own machine does not have the module's Python packages yet. In VS Code's terminal, with the new folder open, run:

```
pip install -r MN5813/2026-27/requirements.lock
```

Use `pip3` on macOS if `pip` is not found. Do not install from `requirements.txt`.


## Everything else stays the same

Set your git identity in the local copy too. Run the two `git config` commands from [Your workstation, Step 6](./codespaces-start.md#step-6-sign-your-work-git-identity-and-your-first-commit), with your candidate number, not your name.


## Getting help

If something does not work, copy the exact error text and take a screenshot. Post them on <!-- gen:values.yml#links.qa_forum|link:the Moodle forum -->[the Moodle forum](https://moodle.royalholloway.ac.uk/mod/hsuforum/view.php?id=1470467)<!-- /gen --> or bring them to the Week 2 session. If you get stuck, use your Codespace.

---

*Back to the [Your workstation guide](./codespaces-start.md) · [module overview](../README.md).*

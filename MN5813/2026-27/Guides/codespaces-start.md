# Your workstation: GitHub Codespaces

*Your first task at [Runnymede Analytics](./glossary.md#term-runnymede-analytics): Open your workstation. Everything the firm uses is already installed.*

> ⚠️ **Draft:** This page is a draft. It will be confirmed in Week 3.

This guide assumes no experience with code editors, terminals, or git (the tool that records versions of your work). You build the workstation with the class in the Week 2 workshop. Step 1 happens a week earlier, in the Week 1 workshop, because GitHub's student verification takes days. Follow the steps in order and tick the checklist as you go. If something goes wrong, say so in the workshop or post on <!-- gen:values.yml#links.qa_forum|link:the Moodle forum -->[the Moodle forum](https://moodle.royalholloway.ac.uk/mod/hsuforum/view.php?id=1470467)<!-- /gen -->.

A GitHub Codespace is a complete workstation that runs in your browser. It holds the VS Code editor, Python, GitHub Copilot (your AI [Associate](./glossary.md#term-associate)), and [SpecStory](./glossary.md#term-specstory) (a recorder that saves each AI session as a text file). It works the same on a five-year-old laptop, a Chromebook, or a lab machine. You install nothing on your own computer.

The time budget is about 30 to 40 minutes, plus a wait of up to a few days for GitHub's student verification.

## ⭐ The checklist

Copy this into your `QuestLog.md` and tick items off as you go. When all ten are ticked, claim the **[Workstation Ready](./glossary.md#term-workstation-ready) ⭐** [badge](./glossary.md#term-badge).

- [ ] 1. GitHub account created (with your university email added)
- [ ] 2. GitHub Student Developer Pack application **submitted** (Copilot Free covers you while you wait)
- [ ] 3. Your own **private repository** created from the student repository and shared with the staff account
- [ ] 4. Repository opened in a **Codespace**: It finished building and VS Code loaded in your browser
- [ ] 5. Signed in to **GitHub Copilot**, asked it one question, and got an answer
- [ ] 6. **SpecStory** checked: Had a chat, found the transcript in `.specstory/history/`
- [ ] 7. Git identity set to your **candidate number**
- [ ] 8. First **<!-- plain-language: everyday commit -->commit and push** made: Your work is saved back to GitHub
- [ ] 9. Codespace **stopped** (so it does not use your free hours while you are away)
- [ ] 10. One stage of **[Quest](./glossary.md#term-quest) 02** run in the Codespace, transcript saved

You do items 1 and 2 in the Week 1 workshop and items 3 to 10 with the class in the Week 2 workshop.

## Step 1: GitHub account and Student Developer Pack

You do this step with staff in the Week 1 workshop. GitHub is where your project and your Codespace live. Your GitHub account also signs you in to Copilot. The **GitHub Student Developer Pack** gives verified students the **GitHub Copilot Student** plan free, plus extra Codespaces hours.

> ⚠️ **Apply in Week 1.** GitHub's verification can take several days. **Copilot Free needs no verification and covers everything this module asks of you.** So nothing waits on the Pack.

### 1a. Create the account

1. Go to [github.com](https://github.com/) and choose **Sign up**
2. Pick a username you would be happy to show a future employer
3. Register with any email. Then **add your university email** (`...@live.rhul.ac.uk` or `...@rhul.ac.uk`) under your email settings and verify it. The Student Pack checks for an academic email

### 1b. Apply for the Student Developer Pack

1. Go to [education.github.com/pack](https://education.github.com/pack) and choose to get student benefits
2. Sign in, select your university email, and give Royal Holloway, University of London as your institution
3. If asked for proof of enrolment, use a photo of your student ID or an enrolment letter showing your name, institution, and current dates
4. Submit. GitHub emails you when it decides. You can check any time at [education.github.com](https://education.github.com/)

> 💡 While you wait, use **Copilot Free**. Details are under "Copilot Free" at [docs.github.com/en/copilot](https://docs.github.com/en/copilot). When your Pack is approved, turn on the free Copilot Student plan in your GitHub settings.

## Step 2: Create your own repository

Your work lives in a **repository** ("repo"), a project folder GitHub keeps for you. You make your own from the module's student repository. It stays private to you and the module team.

1. Open <!-- gen:values.yml#links.student_repository|link:the student repository -->[the student repository](https://github.com/REPPL/Teaching)<!-- /gen --> on GitHub. Sign in with your GitHub account from Step 1 if prompted
2. Click the green **Use this template** button, then choose **Create a new repository**
3. Leave **Owner** as your own account. Type a name for the repository, such as `mn5813-work`
4. Choose **Private**, then click **Create repository**. GitHub opens your new repository's page
5. On that page, open **Settings**, then **Collaborators**, and click **Add people**. Add the staff account named on the <!-- gen:values.yml#module.code -->MN5813<!-- /gen --> Moodle page

You can always return to your repository from your GitHub profile under **Your repositories**.

> 💡 Your repository starts with the module materials and the workstation setup. The materials sit in the folder **<!-- gen:values.yml#module.code -->MN5813<!-- /gen -->/<!-- gen:values.yml#module.year -->2026-27<!-- /gen -->/**. The tools in the next steps are ready when your Codespace opens.

## Step 3: Open your workstation (create a Codespace)

1. On your repository page, click the green **`< > Code`** button
2. Choose the **Codespaces** tab, then **Create codespace on main**
3. Wait while it builds. The first build takes a few minutes and shows a scrolling progress log. This happens only the first time. When it finishes, VS Code opens in your browser

The **Explorer** panel on the left lists your project's files, including all the week folders. The large area is where you read and edit. To open a **terminal** (a place to type commands), choose **New Terminal** from the **Terminal** menu. You can also press `` Ctrl+` `` (Control and backtick, top-left of most keyboards).

> ♿ Codespaces in the browser is the same VS Code as the desktop app, including its screen-reader support. If you use a screen reader, turn on Screen Reader Mode when prompted. You can also open the Command Palette (VS Code's search box for commands, `Ctrl/Cmd+Shift+P`) and choose "Toggle Screen Reader Accessibility Mode".

## Step 3a: Connect the materials

Each week's new materials arrive from the student repository. You connect your repository to it once. Do this straight after Step 3, before you change any file.

Open a terminal (choose **New Terminal** from the **Terminal** menu) and run these two commands:

```
git remote add materials https://github.com/REPPL/Teaching.git
git pull materials main --allow-unrelated-histories
```

The first command gives the student repository the short name `materials`. The second brings in its history. Your repository began as a separate copy, so git needs `--allow-unrelated-histories` to join the two histories once. You never need that option again.

If git reports a conflict here, follow steps 1, 3, and 4 under "If git reports a conflict" below. Then run the second command again.

## Each week: New materials

> 📅 **Each week**
>
> Each week's folder arrives at the start of its teaching week. To get it, run this in the terminal:
>
> ```
> git pull materials main
> ```
>
> - **Copy a notebook into the `work/` folder before you open it.** For example: `cp MN5813/2026-27/Week/02/Quest.ipynb work/Week02-Quest.ipynb`
> - **Name each copy after its week.** A later week's `Quest.ipynb` then cannot overwrite it
> - **Open and change only your copy.** Your copies in `work/` are yours to keep
> - **Never edit the originals** in **<!-- gen:values.yml#module.code -->MN5813<!-- /gen -->/<!-- gen:values.yml#module.year -->2026-27<!-- /gen -->/**. Next week's materials arrive on top of them, and an edited original can block the update

### If git reports a conflict

This happens only when you changed an original file. Git prints the file's path. Run these steps in the terminal, replacing `<file>` with that path:

1. If git printed the word `CONFLICT`, run `git merge --abort`. This undoes the unfinished pull
2. Keep your edits: Run `cp <file> work/my-edits.md`. Choose a name that is not already in `work/`
3. Put back the original: Run `git checkout materials/main -- <file>`
4. Save the change: Run `git add .`, then `git commit -m "Move my edits into work"`
5. Pull again: Run `git pull materials main`

If git names more than one file, repeat steps 2 and 3 for each file. If the pull still fails, copy the exact message and post it on the Moodle forum.

## Step 4: Meet your Associate (GitHub Copilot)

You opened the Codespace signed in to GitHub, so Copilot is usually ready at once.

1. Find the **Copilot chat icon** in the top or left bar and open the chat panel. If it asks you to sign in or enable Copilot, use your Step 1 account. Either the student plan or Copilot Free works
2. Ask it something real, for example *"Explain what a Python list is, three different ways"*
3. If it answers, your Associate is ready. When you type code later, grey **inline suggestions** appear. Press `Tab` to accept, `Esc` to dismiss

## Step 5: Check your record (SpecStory)

The module requires an **[AI Use Record](./glossary.md#term-ai-use-record)**, described in the [AI guide](./ai-guide.md), section "7. The AI Use Record". SpecStory saves the transcripts for it automatically. Confirm it is working.

1. With your project open, have a short, real exchange in Copilot Chat. Step 4 counts
2. In the Explorer panel, find a folder named **`.specstory`** containing **`history/`**. Folders starting with a dot are hidden by convention, but VS Code shows them
3. Open the newest file inside `history/`. It is a plain markdown file of your prompts and the Associate's replies, timestamped and searchable

SpecStory records only your AI conversations in this project, nothing else on your workstation. Each session becomes one markdown file in your repo. That transcript is your [quest](./glossary.md#term-quest) record and the evidence behind your AI Use Record in both assessments. It is the automatic version of the [Prompt Diary](./glossary.md#term-prompt-diary) you kept by hand in Quest 01. After each session, check that the file is in `.specstory/history/`. Full details are at [docs.specstory.com](https://docs.specstory.com/).

If SpecStory does not suit you, any consistent, honest, and dated way of keeping the same record satisfies the requirement. Talk to the module team.

## Step 6: Sign your work (git identity and your first commit)

Your Codespace saves your files as you go. To send your work back to GitHub, you make a **<!-- plain-language: everyday commit -->commit** (a saved snapshot of your files) and **push** it (send it to GitHub). GitHub backs it up, and the marker collects it from there. <!-- plain-language: everyday commit -->Commit early and often.

1. **Set your identity to your candidate number.** Open a terminal (choose **New Terminal** from the **Terminal** menu) and run these commands, replacing `123456` with your real candidate number:

   ```
   git config user.name "123456"
   git config user.email "123456@rhul.invalid"
   ```

   The module marks you by candidate number, never by name

2. **Make your first <!-- plain-language: everyday commit -->commit and push.** Still in the terminal:

   ```
   git add .
   git commit -m "Workstation ready"
   git push
   ```

   In a Codespace, git is already signed in to GitHub, so `push` works with no passwords to set up

If it worked, the <!-- plain-language: everyday commit -->commit line reports something like `12 files changed` and `push` ends without an error. Refresh your repository page on github.com and your <!-- plain-language: everyday commit -->commit is there. This is how your work reaches us: Your notebook and your `.specstory/` transcripts, committed and pushed. Each assessment also needs a PDF of your report uploaded to Moodle, and that upload is what counts for the deadline. The assessment briefs have the details.

> 💡 Prefer buttons to typing? VS Code's **Source Control** panel (the branch icon in the left bar) does the same thing. Stage the changes (mark them for the <!-- plain-language: everyday commit -->commit), type a message, click **<!-- plain-language: everyday commit -->Commit**, then **Sync/Push**.

## Step 7: Stopping your workstation

Codespaces gives you a **free monthly allowance** of running hours. Your workstation spends them only while it is running. When you finish for the day, stop it. Your files are kept.

1. Open the Command Palette (`Ctrl/Cmd+Shift+P`)
2. Type **"Codespaces: Stop Current Codespace"** and select it. Closing the browser tab also stops it after a short idle period
3. Next time, open your repo, click **`< > Code`**, choose **Codespaces**, and click your existing Codespace to resume it. Resuming is much faster than the first build

You can see your Codespaces, their status, and your usage at [github.com/codespaces](https://github.com/codespaces/). Current allowances and how billing works are at [docs.github.com/codespaces](https://docs.github.com/en/codespaces).

For checklist item 10, open the Week 2 Quest in this Codespace and run one stage.

## Troubleshooting

Optional, for your own time: Use it when you need it.

- **The Codespace never finishes building, or fails with an error.** Reload the browser tab. If it still fails, delete the Codespace at [github.com/codespaces](https://github.com/codespaces/) (the three-dot `...` menu, then **Delete**) and create a fresh one from your repo. If a fresh one also fails, say so in the workshop or on the Moodle forum
- **Copilot says "not signed in" or never suggests anything.** Open the Accounts menu (person icon, bottom-left) and confirm you are signed in with your Step 1 GitHub account. If Copilot is disabled in the status bar (the strip along the bottom of the window), click it and enable it
- **Student Pack verification still pending, or refused.** Use **Copilot Free** for now. Turn on the Copilot Student plan if the Pack is approved. If GitHub refuses your application, use Copilot Free plus a second tool. The second tools are in the [AI guide](./ai-guide.md), section "If you cannot get Copilot, or run out of chat". Tell the module team as well
- **`.specstory/history/` never appears.** It is created on your first AI session in this project. Have a Copilot chat first, then reload the window (Command Palette, "Developer: Reload Window"). If it still does not appear, keep your record another way (Step 5) and tell the module team
- **`git pull materials main` says `'materials' does not appear to be a git repository`.** You have not connected the materials yet. Run the two commands in Step 3a
- **`git push` asks for a password or fails.** Reload the window. If it persists, sign out and back in to GitHub from the Accounts menu, then retry
- **"You have run low on Codespaces hours".** Stop your Codespace whenever you are not using it (Step 7). If you are out of hours, post on the Moodle forum. The Student Pack (Step 1) raises your allowance if it is approved
- **Everything is slow or laggy in the browser.** Codespaces needs a steady connection, not a fast computer. Try a wired or eduroam connection and close other heavy browser tabs
- **I closed the tab or lost my place.** Nothing is lost. Resume your Codespace as in Step 7

## Getting help

Optional, for your own time: Use it when you need it.

- **The workshop.** Bring your laptop. Say something the moment your screen stops matching the one at the front
- **<!-- gen:values.yml#links.qa_forum|link:The Moodle forum -->[The Moodle forum](https://moodle.royalholloway.ac.uk/mod/hsuforum/view.php?id=1470467)<!-- /gen -->.** Post problems as they happen. Answers there help the whole cohort
- **What to bring or post.** Bring the **exact error text**, a **screenshot** of the whole window, and the step you were on. Copy and paste the error text; do not retype it in your own words
- **Ask your Associate first.** Paste the error into Copilot Chat and ask what it means. Check its answer before you act on it

Every quest from here on runs in this workstation.

---

*Next: The Week 2 Exercises notebook, driving lessons for your new workstation. Back to the [module overview](../README.md).*

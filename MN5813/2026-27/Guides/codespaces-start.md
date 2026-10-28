# Your workstation: GitHub Codespaces

*Your first task at [Runnymede Analytics](./glossary.md#term-runnymede-analytics): Open your workstation. Everything the firm uses is already installed.*

> ⚠️ **Draft:** This page is a draft. It will be confirmed at a later date.

You build the workstation with the class in the Week 2 workshop. Follow the steps in order and tick the checklist as you go. If something goes wrong, say so in the workshop or post on <!-- gen:values.yml#links.qa_forum|link:the Moodle forum -->[the Moodle forum](https://moodle.royalholloway.ac.uk/mod/hsuforum/view.php?id=1470467)<!-- /gen -->.

A GitHub Codespace is a complete workstation that runs in your browser. It includes the VS Code editor, Python, and GitHub Copilot (your AI [Associate](./glossary.md#term-associate)). You install nothing on your own computer.

The time budget is about 30 to 40 minutes, plus a wait of up to a few days for GitHub's student verification.


## ⭐ The checklist

Copy this into your `QuestLog.md` and tick items off as you go. When all ten are ticked, claim the **[Workstation Ready](./glossary.md#term-workstation-ready) ⭐** [badge](./glossary.md#term-badge).

- [ ] 1. GitHub account created (with your university email added)
- [ ] 2. GitHub Student Developer Pack application **submitted** (Copilot Free covers you while you wait)
- [ ] 3. Your own **private repository** created from the student repository and shared with the staff account
- [ ] 4. Repository opened in a **Codespace**: It finished building and VS Code loaded in your browser
- [ ] 5. Signed in to **GitHub Copilot**, asked it one question, and got an answer
- [ ] 6. **[Prompt Diary](./glossary.md#term-prompt-diary)** started: Your Step 4 chat pasted into `PromptDiary.md`, under today's date
- [ ] 7. Git identity set to your **candidate number**
- [ ] 8. First **<!-- plain-language: everyday commit -->commit and push** made: Your work is saved back to GitHub
- [ ] 9. Codespace **stopped** (so it does not use your free hours while you are away)
- [ ] 10. One stage of **[Quest](./glossary.md#term-quest) 02** run in the Codespace, and its exchanges added to your Prompt Diary

You do items 1 and 2 in the Week 1 workshop and items 3 to 10 with the class in the Week 2 workshop.


## Step 1: GitHub account and Student Developer Pack

You do this step with me in the Week 1 workshop. The **GitHub Student Developer Pack** gives verified students the **GitHub Copilot Student** plan free, plus extra Codespaces hours.

> ⚠️ **Apply in Week 1.** GitHub's verification can take several days. **Copilot Free needs no verification and covers everything this module asks of you.**


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

Your work lives in a **repository** ("repo"), a project folder GitHub keeps for you. You make your own from the module's student repository. It stays private to you and me.

1. Open <!-- gen:values.yml#links.student_repository|link:the student repository -->[the student repository](https://github.com/REPPL/Teaching)<!-- /gen --> on GitHub. Sign in with your GitHub account from Step 1 if prompted
2. Click the green **Use this template** button, then choose **Create a new repository**
3. Leave **Owner** as your own account. Type a name for the repository, such as `mn5813-work`
4. Choose **Private**, then click **Create repository**. GitHub opens your new repository's page
5. On that page, open **Settings**, then **Collaborators**, and click **Add people**. Add the staff account named on the <!-- gen:values.yml#module.code -->MN5813<!-- /gen --> Moodle page
6. Click the **Actions** tab. If GitHub shows a button to enable workflows, click it. This lets new materials arrive by themselves (Step 3a)

> 💡 The materials sit in the folder **<!-- gen:values.yml#module.code -->MN5813<!-- /gen -->/<!-- gen:values.yml#module.year -->2026-27<!-- /gen -->/**.


## Step 3: Open your workstation (create a Codespace)

1. On your repository page, click the green **`< > Code`** button
2. Choose the **Codespaces** tab, then **Create codespace on main**
3. Wait while it builds. The first build takes a few minutes. When it finishes, VS Code opens in your browser

The **Explorer** panel on the left lists your project's files. To open a **terminal** (a place to type commands), choose **New Terminal** from the **Terminal** menu. You can also press `` Ctrl+` `` (Control and backtick, top-left of most keyboards).

> ♿ If you use a screen reader, turn on Screen Reader Mode when prompted. You can also open the Command Palette (VS Code's search box for commands, `Ctrl/Cmd+Shift+P`) and choose "Toggle Screen Reader Accessibility Mode".


## Step 3a: Get new materials

New materials arrive in your repository by themselves. A helper called **Get new materials** runs every afternoon.

The helper follows these rules:

- It adds every new file
- It updates every file you have not changed
- It never touches a file you changed. If I correct that file, the new version is saved next to yours. Its name has `.updated` in it, such as `Quest.updated.ipynb` next to your `Quest.ipynb`

To get new materials straight away, run the helper yourself:

1. Open your repository on GitHub
2. Click the **Actions** tab
3. Click **Get new materials** in the list on the left
4. Click **Run workflow**, then the green **Run workflow** button
5. Wait about a minute for a green tick

To bring the new files into your Codespace, click the circling arrows next to `main` in the status bar at the bottom of the window. Do this each time you open your Codespace.


### Adding Get new materials to an older repository

A repository made before the helper existed needs it added once. You do this on GitHub, not in the Codespace.

1. Open [the helper's file](https://github.com/REPPL/Teaching/blob/main/.github/workflows/get-materials.yml) in the student repository <!-- values-guard: allow: one file's address inside the student repository -->
2. Click **Copy raw file**, the button with two overlapping squares above the file
3. Open your own repository. Click **Add file**, then **Create new file**
4. In the name box, type `.github/workflows/get-materials.yml`. Each `/` starts a new folder
5. Click in the large box below it and paste
6. Click **<!-- plain-language: everyday commit -->Commit changes**, then **<!-- plain-language: everyday commit -->Commit changes** again
7. Run the helper once, as in Step 3a

If you connected the materials with git commands earlier, you can stop using them now. Nothing needs undoing.


## Each week: New materials

> 📅 **Each week**
>
> Each week's folder arrives in your repository on the Monday afternoon of its teaching week. Open your Codespace with the **Open in GitHub Codespaces** button at the top of any notebook in your repository.
>
> - **Look out for `.updated` files.** One appears when I correct a file you changed. Compare the two and keep what you need
> - **Use the `work/` folder for extra copies.** Keep each copy in a folder for its week, as [Your work](../../../work/README.md) explains
> - **End each session with <!-- plain-language: everyday commit -->Commit and Sync.** Step 6 shows how. Your work is then safe on GitHub


## Step 4: Meet your Associate (GitHub Copilot)

1. Find the **Copilot chat icon** in the top or left bar and open the chat panel. If it asks you to sign in or enable Copilot, use your Step 1 account
2. Ask it something real, for example *"Explain what a Python list is, three different ways"*
3. If it answers, your Associate is ready. When you type code later, grey **inline suggestions** appear. Press `Tab` to accept, `Esc` to dismiss


## Step 5: Start your Prompt Diary

Your Prompt Diary is the evidence behind your **[AI Use Record](./glossary.md#term-ai-use-record)**. From today, it lives in your repository.

1. In the Explorer panel, create a file named `PromptDiary.md` at the top level of your repository. Your `QuestLog.md` goes in the same place
2. Type today's date as a heading, such as `## 12 October`. Below it, paste your Step 4 question and Copilot's answer
3. Add one line of your own: What you asked, and what you made of the answer

After each AI session, add a dated entry. The [AI guide](./ai-guide.md), section "6. Your record is your evidence", explains what to keep.


## Step 6: Sign your work (git identity and your first commit)

Your Codespace saves your files as you go. To send your work back to GitHub, you make a **<!-- plain-language: everyday commit -->commit** (a saved snapshot of your files) and **push** it (send it to GitHub). <!-- plain-language: everyday commit -->Commit early and often.

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

If it worked, the <!-- plain-language: everyday commit -->commit line reports something like `12 files changed` and `push` ends without an error. Refresh your repository page on github.com and your <!-- plain-language: everyday commit -->commit is there. The individual report also needs a PDF uploaded to Moodle, and that upload is what counts for the submission date. The [assessment briefs](../Assessment/README.md) have the details.

> 💡 Prefer buttons to typing? VS Code's **Source Control** panel (the branch icon in the left bar) does the same thing. Stage the changes, type a message, click **<!-- plain-language: everyday commit -->Commit**, then **Sync/Push**.


## Step 7: Stopping your workstation

Codespaces gives you a **free monthly allowance** of running hours. When you finish for the day, stop it. Your files are kept.

1. Open the Command Palette (`Ctrl/Cmd+Shift+P`)
2. Type **"Codespaces: Stop Current Codespace"** and select it. Closing the browser tab also stops it after a short idle period
3. Next time, open your repo, click **`< > Code`**, choose **Codespaces**, and click your existing Codespace to resume it

You can see your Codespaces, their status, and your usage at [github.com/codespaces](https://github.com/codespaces/). Current allowances and how billing works are at [docs.github.com/codespaces](https://docs.github.com/en/codespaces).

For checklist item 10, open [the Week 2 Quest](../Week/02/Quest.ipynb) in this Codespace and run one stage.


## Troubleshooting

Optional, for your own time: Use it when you need it.

- **The Codespace never finishes building, or fails with an error.** Reload the browser tab. If it still fails, delete the Codespace at [github.com/codespaces](https://github.com/codespaces/) (the three-dot `...` menu, then **Delete**) and create a fresh one from your repo. If a fresh one also fails, say so in the workshop or on the Moodle forum
- **Copilot says "not signed in" or never suggests anything.** Open the Accounts menu (person icon, bottom-left) and confirm you are signed in with your Step 1 GitHub account. If Copilot is disabled in the status bar (the strip along the bottom of the window), click it and enable it
- **Student Pack verification still pending, or refused.** Use **Copilot Free** for now. Turn on the Copilot Student plan if the Pack is approved. If GitHub refuses your application, use Copilot Free plus a second tool. The second tools are in the [AI guide](./ai-guide.md), section "If you cannot get Copilot, or run out of chat". Tell me as well
- **There is no Get new materials in the Actions tab.** Your repository was made before the helper existed. Add it once, as in "Adding Get new materials to an older repository" above
- **Get new materials shows a red cross.** Click the run, then the step with the red cross. Copy the message and post it on the Moodle forum. A failed run changes none of your files
- **The status bar arrows report a conflict.** This happens when you change a file in your Codespace without syncing, and the helper updates it on GitHub. Post a screenshot on the Moodle forum before you click anything else
- **`git push` asks for a password or fails.** Reload the window. If it persists, sign out and back in to GitHub from the Accounts menu, then retry
- **"You have run low on Codespaces hours".** Stop your Codespace whenever you are not using it (Step 7). If you are out of hours, post on the Moodle forum. The Student Pack (Step 1) raises your allowance if it is approved
- **Everything is slow or laggy in the browser.** Codespaces needs a steady connection, not a fast computer. Try a wired or eduroam connection and close other heavy browser tabs
- **I closed the tab or lost my place.** Nothing is lost. Resume your Codespace as in Step 7


## Getting help

Optional, for your own time: Use it when you need it.

- **The workshop.** Bring your laptop. Say something the moment your screen stops matching the one at the front
- **<!-- gen:values.yml#links.qa_forum|link:The Moodle forum -->[The Moodle forum](https://moodle.royalholloway.ac.uk/mod/hsuforum/view.php?id=1470467)<!-- /gen -->.** Post problems as they happen
- **What to bring or post.** Bring the **exact error text**, a **screenshot** of the whole window, and the step you were on
- **Ask your Associate first.** Paste the error into Copilot Chat and ask what it means. Check its answer before you act on it

---

*Next: [The Week 2 Exercises notebook](../Week/02/Exercises.ipynb), driving lessons for your new workstation. Back to the [module overview](../README.md).*

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DAY 4: Git & GitHub — Complete Guide
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# This file is your RUNNABLE REFERENCE for Git.
# Run it anytime to see a summary of all Git commands!
#
# Topics:
#   1. Git Basics — init, add, commit, status, log
#   2. Remote & GitHub — push, pull, clone
#   3. .gitignore — hiding files from Git
#   4. Branching — working on features safely
#   5. Merging — combining branches
#   6. Pull Requests — team collaboration on GitHub
#   7. Undoing Mistakes — reset, revert, stash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def section_1():
    """Git Basics — The Foundation"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║  SECTION 1: Git Basics                                       ║
╚══════════════════════════════════════════════════════════════╝

  What is Git?
  ────────────
  Git is a VERSION CONTROL system. It tracks every change you make
  to your code, so you can:
    - Go back to any previous version
    - See who changed what and when
    - Work on new features without breaking working code

  Think of it as: UNLIMITED UNDO for your entire project + a time machine.

  The 3 Stages of Git:
  ────────────────────
  ┌──────────────┐    git add     ┌──────────────┐   git commit   ┌──────────────┐
  │  Working Dir  │ ──────────▶  │  Staging Area │ ──────────▶   │  Repository   │
  │  (your files) │              │  (ready to go) │               │ (saved forever)│
  └──────────────┘              └──────────────┘               └──────────────┘

  Working Directory: Your actual files (what you see in VS Code)
  Staging Area:      Files you've marked to be saved (git add)
  Repository:        The permanent history of all your commits


  Essential Commands:
  ──────────────────
  git init                     Create a new Git repo in current folder
  git status                   See what's changed (modified, staged, untracked)
  git add <file>               Stage a specific file
  git add .                    Stage ALL changed files
  git add days/day4/           Stage only files in a specific folder
  git commit -m "message"      Save staged files with a description
  git log                      See commit history
  git log --oneline            See compact commit history
  git log -n 5                 See last 5 commits only
  git diff                     See what changed in your files (before staging)
  git diff --staged            See what's staged and ready to commit


  Commit Message Best Practices:
  ─────────────────────────────
  GOOD:
    git commit -m "Add user authentication with JWT tokens"
    git commit -m "Fix API timeout when processing large files"
    git commit -m "Day 3 complete: Python Advanced"

  BAD:
    git commit -m "fix"
    git commit -m "stuff"
    git commit -m "asdfgh"

  Format: <action verb> + <what you did>
  """)


def section_2():
    """Remote & GitHub — Push, Pull, Clone"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║  SECTION 2: Remote & GitHub                                  ║
╚══════════════════════════════════════════════════════════════╝

  What is a Remote?
  ─────────────────
  A "remote" is a copy of your repo stored online (GitHub, GitLab, etc.)
  Your local repo and the remote stay in sync through push/pull.

  ┌──────────────┐    git push    ┌──────────────┐
  │  Your PC      │ ─────────────▶│  GitHub       │
  │  (local)      │◀─────────────│  (remote)     │
  └──────────────┘    git pull    └──────────────┘


  Essential Commands:
  ──────────────────
  git remote -v                     See your remote URLs
  git push                          Upload commits to GitHub
  git push origin main              Push to the "main" branch on "origin"
  git pull                          Download latest changes from GitHub
  git clone <url>                   Download an entire repo from GitHub

  Clone Example:
  ──────────────
  git clone https://github.com/luckyyadav29/AI-Engineer-OS.git
  # This downloads the ENTIRE repo to your computer

  Your Remote Setup:
  ──────────────────
  origin = https://github.com/luckyyadav29/AI-Engineer-OS.git
  "origin" is just a nickname for the GitHub URL. You can have multiple remotes.


  The Full Workflow (What you've been doing):
  ───────────────────────────────────────────
  1. Make changes to files
  2. git add days/day4/          (stage only day4 files)
  3. git commit -m "Day 4: ..."  (save locally with a message)
  4. git push                    (upload to GitHub)
  """)


def section_3():
    """.gitignore — Hiding Files from Git"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║  SECTION 3: .gitignore                                       ║
╚══════════════════════════════════════════════════════════════╝

  What is .gitignore?
  ───────────────────
  A file that tells Git: "IGNORE these files. Don't track them. Ever."

  Why?
  ────
  Some files should NEVER be on GitHub:
    - API keys & secrets (anyone can steal them!)
    - venv/ folder (huge, everyone creates their own)
    - __pycache__/ (auto-generated junk)
    - .env files (passwords, tokens)
    - Large datasets (too big for GitHub)


  How it works:
  ─────────────
  Create a file named ".gitignore" in your repo root:

  # Python junk
  __pycache__/
  *.pyc
  *.pyo

  # Virtual environment
  venv/
  .venv/
  env/

  # API keys & secrets (CRITICAL!)
  .env
  *.key
  secrets.json

  # IDE settings
  .vscode/
  .idea/

  # OS files
  .DS_Store
  Thumbs.db

  # Large files
  *.csv
  *.zip
  data/


  IMPORTANT RULE FOR AI ENGINEERING:
  ──────────────────────────────────
  NEVER commit API keys! If your OpenAI key gets on GitHub,
  someone WILL find it and run up your bill.
  Always use .env files + .gitignore.

  # Example .env file (NEVER committed):
  OPENAI_API_KEY=sk-abc123...
  GEMINI_API_KEY=AIza...

  # In your Python code:
  import os
  api_key = os.getenv("OPENAI_API_KEY")
  """)


def section_4():
    """Branching — Working on Features Safely"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║  SECTION 4: Branching                                        ║
╚══════════════════════════════════════════════════════════════╝

  What is a Branch?
  ─────────────────
  A branch is a PARALLEL COPY of your code.
  You can experiment on a branch without affecting the main code.

  Think of it like:
    main     = the LIVE version (working, stable)
    feature  = your EXPERIMENT (might break things)

  When the experiment works → merge it into main.
  When it fails → delete the branch. Main is untouched!


  Visual:
  ───────
  main:    ──●──●──●──●──●──●──●──  (stable, always works)
                    \\              /
  feature:           ●──●──●──●──   (your experiment)
                    branch    merge


  Essential Commands:
  ──────────────────
  git branch                        List all branches (* = current)
  git branch feature-name           Create a new branch
  git checkout feature-name         Switch to that branch
  git checkout -b feature-name      Create AND switch (shortcut!)
  git branch -d feature-name        Delete a branch (after merging)


  Real Example:
  ─────────────
  # You want to add a new AI model to your app:

  git checkout -b add-gemini-model       # Create & switch to new branch
  # ... make your changes ...
  git add .
  git commit -m "Add Gemini model support"
  git checkout main                      # Switch back to main
  git merge add-gemini-model             # Merge the feature in
  git branch -d add-gemini-model         # Clean up: delete the branch


  Important Rules:
  ────────────────
  1. NEVER work directly on main for new features
  2. Create a branch → work on it → merge when ready
  3. Branch names should be descriptive: "fix-login-bug", "add-rag-pipeline"
  """)


def section_5():
    """Merging — Combining Branches"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║  SECTION 5: Merging                                          ║
╚══════════════════════════════════════════════════════════════╝

  What is Merging?
  ────────────────
  Taking changes from one branch and putting them into another.

  How to merge:
  ─────────────
  git checkout main              # Step 1: Go to the branch you want to merge INTO
  git merge feature-branch       # Step 2: Pull changes FROM the feature branch


  Merge Conflicts:
  ────────────────
  When TWO branches edit the SAME line, Git can't decide which to keep.
  It marks the conflict and asks YOU to fix it.

  What a conflict looks like:
  ──────────────────────────
  <<<<<<< HEAD
  model = "gpt-4"            ← What's on main
  =======
  model = "gemini-pro"       ← What's on your branch
  >>>>>>> feature-branch

  How to fix:
  1. Open the file with the conflict
  2. Choose which version to keep (or combine them)
  3. Delete the <<<<<<, ======, >>>>>> markers
  4. git add the fixed file
  5. git commit


  After fixing:
  ─────────────
  model = "gemini-pro"       ← You chose this one (or write something new)

  Then:
  git add .
  git commit -m "Resolve merge conflict in config"
  """)


def section_6():
    """Pull Requests — Team Collaboration"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║  SECTION 6: Pull Requests (PRs)                              ║
╚══════════════════════════════════════════════════════════════╝

  What is a Pull Request?
  ───────────────────────
  A PULL REQUEST is a way to propose changes on GitHub.
  Instead of merging directly, you:
    1. Push your branch to GitHub
    2. Create a PR (Pull Request) on GitHub's website
    3. Others review your code
    4. If approved → merge into main

  This is how ALL real teams work!


  How to create a PR:
  ──────────────────
  # Step 1: Create a branch and make changes
  git checkout -b my-feature
  # ... make changes, add, commit ...

  # Step 2: Push the branch to GitHub
  git push origin my-feature

  # Step 3: Go to GitHub.com → your repo
  # You'll see: "my-feature had recent pushes — Compare & pull request"
  # Click it → Write a description → Create Pull Request

  # Step 4: After review → Merge on GitHub
  # Click "Merge pull request" → "Confirm merge"

  # Step 5: Clean up locally
  git checkout main
  git pull                          # Get the merged changes
  git branch -d my-feature          # Delete local branch


  PR Best Practices:
  ──────────────────
  - Write clear titles: "Add RAG pipeline with ChromaDB"
  - Describe what changed and why
  - Keep PRs small (easier to review)
  - Reference issues: "Fixes #12"
  """)


def section_7():
    """Undoing Mistakes — Git Safety Net"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║  SECTION 7: Undoing Mistakes                                 ║
╚══════════════════════════════════════════════════════════════╝

  "I messed up!" — Git has your back:
  ────────────────────────────────────

  UNDO unstaged changes (go back to last commit):
  git checkout -- <file>             Discard changes in one file
  git checkout -- .                  Discard ALL changes

  UNDO staged files (remove from staging):
  git reset HEAD <file>              Unstage one file
  git reset HEAD .                   Unstage everything

  UNDO last commit (keep the changes):
  git reset --soft HEAD~1            Undo commit, keep changes staged

  UNDO last commit (discard changes completely):
  git reset --hard HEAD~1            WARNING: Changes are GONE forever!

  SAVE work temporarily (stash):
  git stash                          Save current changes aside
  git stash pop                      Bring them back

  Example stash workflow:
  ───────────────────────
  # You're working on feature A, but need to urgently fix a bug:
  git stash                       # Save feature A work
  git checkout main               # Switch to main
  # ... fix the bug, commit ...
  git checkout feature-a          # Go back
  git stash pop                   # Restore your saved work


  GOLDEN RULE:
  ────────────
  If you're unsure, run "git status" first!
  It always tells you what's going on and suggests what to do.
  """)


def section_summary():
    """Quick Reference Card"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║  GIT CHEAT SHEET                                             ║
╚══════════════════════════════════════════════════════════════╝

  BASICS:
  git init                         Start tracking a folder
  git status                       Check what's changed
  git add <file>                   Stage a file
  git add .                        Stage everything
  git commit -m "msg"              Save with a message
  git log --oneline                View history

  REMOTE:
  git push                         Upload to GitHub
  git pull                         Download from GitHub
  git clone <url>                  Download entire repo

  BRANCHES:
  git branch                       List branches
  git checkout -b <name>           Create & switch to branch
  git checkout main                Switch to main
  git merge <branch>               Merge branch into current
  git branch -d <name>             Delete branch

  UNDO:
  git checkout -- <file>           Discard file changes
  git reset HEAD <file>            Unstage a file
  git stash / git stash pop        Save/restore work temporarily

  SAFETY:
  git status                       Always check first!
  git log --oneline                See what happened
  git diff                         See exact changes
""")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RUN ALL SECTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if __name__ == "__main__":
    print("Day 4: Git & GitHub")
    print("=" * 55)

    section_1()    # Git Basics
    section_2()    # Remote & GitHub
    section_3()    # .gitignore
    section_4()    # Branching
    section_5()    # Merging
    section_6()    # Pull Requests
    section_7()    # Undoing Mistakes
    section_summary()  # Cheat Sheet

    print("\n" + "=" * 55)
    print("Day 4 Complete!")
    print("=" * 55)
    print("""
    What you learned:
    1. Git Basics      - add, commit, status, log, diff
    2. Remote/GitHub   - push, pull, clone
    3. .gitignore      - hide sensitive files & junk
    4. Branching       - work on features safely
    5. Merging         - combine branches, resolve conflicts
    6. Pull Requests   - how real teams collaborate
    7. Undoing         - reset, stash, checkout

    Now complete the HANDS-ON EXERCISES in day4_exercises.md!
    """)

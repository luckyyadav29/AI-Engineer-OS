# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DAY 4: HANDS-ON EXERCISES — Do These In Your Terminal!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# These exercises are meant to be done STEP BY STEP in your terminal.
# Read each exercise, then run the git commands yourself.
# After each exercise, ask me to verify your work!
#
# Open your terminal in VS Code (Ctrl + `) and navigate to:
# cd "C:\Users\Lucky Yadav\Desktop\Ai\github repo\AI-Engineer-OS"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


exercises = {
    "Exercise 1": {
        "title": "Git Status & Log (Warm-up)",
        "instructions": """
        Run these commands one by one and observe the output:

        1. git status
           → What does it show? (clean? modified? untracked?)

        2. git log --oneline
           → You should see your Day 1, 2, 3 commits!

        3. git log --oneline -n 3
           → Shows only the last 3 commits

        4. git remote -v
           → Shows your GitHub URL (origin)
        """,
    },

    "Exercise 2": {
        "title": "Understanding Add & Commit",
        "instructions": """
        Let's understand the staging area:

        1. Create a new file: days/day4/test_file.py
           Write anything inside it (e.g., print("hello"))

        2. git status
           → You should see "Untracked files: days/day4/test_file.py"

        3. git add days/day4/test_file.py
           → Stages ONLY this file

        4. git status
           → Now it shows "Changes to be committed" (GREEN!)

        5. Modify test_file.py again (add another line)

        6. git status
           → You'll see the file in BOTH staged AND modified!
           → The staged version is the OLD one, the modified is the NEW one

        7. git add days/day4/test_file.py
           → Now the latest version is staged

        8. git commit -m "Add test file for Day 4 exercise"
           → Saved!
        """,
    },

    "Exercise 3": {
        "title": "Create a .gitignore",
        "instructions": """
        Create a .gitignore file in your repo ROOT:
        (C:\\Users\\Lucky Yadav\\Desktop\\Ai\\github repo\\AI-Engineer-OS\\.gitignore)

        Add these lines:
        ──────────────
        # Python
        __pycache__/
        *.pyc
        *.pyo

        # Virtual Environment
        venv/
        .venv/
        env/

        # API Keys & Secrets
        .env
        *.key
        secrets.json

        # IDE
        .vscode/
        .idea/

        # OS
        .DS_Store
        Thumbs.db
        ──────────────

        Then:
        git add .gitignore
        git commit -m "Add .gitignore for Python project"
        """,
    },

    "Exercise 4": {
        "title": "Your First Branch!",
        "instructions": """
        1. git branch
           → Shows only "* main" (you're on main)

        2. git checkout -b add-day4-feature
           → Creates AND switches to a new branch

        3. git branch
           → Now shows TWO branches! * is on add-day4-feature

        4. Create a new file: days/day4/feature.py
           Write inside it:
           ─────────────────
           # This file was created on a feature branch!

           def my_feature():
               return "This feature was developed safely on a branch!"

           print(my_feature())
           ─────────────────

        5. git add days/day4/feature.py
           git commit -m "Add feature.py on feature branch"

        6. git log --oneline -n 3
           → Your new commit is HERE (on the feature branch)

        7. git checkout main
           → Switch back to main

        8. Check: Does feature.py exist?
           → NO! It only exists on the feature branch!
           → Main is untouched and safe!
        """,
    },

    "Exercise 5": {
        "title": "Merge the Branch",
        "instructions": """
        Now let's bring the feature into main:

        1. Make sure you're on main:
           git checkout main

        2. git merge add-day4-feature
           → This pulls ALL commits from the feature branch into main

        3. Check: Does feature.py exist now?
           → YES! It's been merged into main!

        4. git log --oneline -n 5
           → You can see the merge

        5. git branch -d add-day4-feature
           → Delete the branch (it's merged, we don't need it anymore)

        6. git branch
           → Only "* main" remains
        """,
    },

    "Exercise 6": {
        "title": "Push a Branch & Create a Pull Request",
        "instructions": """
        Let's do it the PROFESSIONAL way — with a Pull Request!

        1. git checkout -b improve-day4-docs
           → Create a new branch

        2. Open days/day4/day4_git_github.py and add a comment at the top:
           # Reviewed and understood by Lucky Yadav

        3. git add days/day4/day4_git_github.py
           git commit -m "Add review note to Day 4 guide"

        4. git push origin improve-day4-docs
           → Push THIS BRANCH to GitHub (not main!)

        5. Go to: https://github.com/luckyyadav29/AI-Engineer-OS
           → You'll see a yellow banner: "improve-day4-docs had recent pushes"
           → Click "Compare & pull request"

        6. Write a title and description:
           Title: "Improve Day 4 documentation"
           Description: "Added review note to the Git guide"

        7. Click "Create pull request"

        8. Click "Merge pull request" → "Confirm merge"

        9. Back in your terminal:
           git checkout main
           git pull
           git branch -d improve-day4-docs
        """,
    },

    "Exercise 7": {
        "title": "Simulate & Resolve a Merge Conflict",
        "instructions": """
        Let's intentionally create a conflict and fix it!

        1. Make sure you're on main. Edit days/day4/feature.py:
           Change the return to: return "Version from MAIN"
           git add .
           git commit -m "Update feature on main"

        2. git checkout -b conflict-branch
           Edit days/day4/feature.py AGAIN:
           Change the return to: return "Version from BRANCH"
           git add .
           git commit -m "Update feature on branch"

        3. git checkout main
           git merge conflict-branch
           → CONFLICT! Git can't decide which version to keep!

        4. Open feature.py — you'll see:
           <<<<<<< HEAD
           return "Version from MAIN"
           =======
           return "Version from BRANCH"
           >>>>>>> conflict-branch

        5. Fix it manually: delete the markers, keep what you want:
           return "Version from BRANCH (merged)"

        6. git add days/day4/feature.py
           git commit -m "Resolve merge conflict in feature.py"

        7. git branch -d conflict-branch
           → Done! Conflict resolved!
        """,
    },
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Print all exercises
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if __name__ == "__main__":
    print("Day 4: Git & GitHub — Hands-On Exercises")
    print("=" * 55)

    for name, exercise in exercises.items():
        print(f"\n{'='*55}")
        print(f"  {name}: {exercise['title']}")
        print(f"{'='*55}")
        print(exercise["instructions"])

    print("\n" + "=" * 55)
    print("""
    EXERCISE ORDER:
    1. Status & Log (warm-up)
    2. Add & Commit (understand staging)
    3. Create .gitignore (protect your secrets!)
    4. Create a branch (safe experimentation)
    5. Merge the branch (bring it together)
    6. Push branch & create a Pull Request on GitHub
    7. Simulate & resolve a merge conflict

    Do them IN ORDER. Ask me after each one to check your work!
    """)

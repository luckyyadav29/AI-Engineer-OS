# Day 4: Git & GitHub

## Topics Covered
1. **Git Basics** — init, add, commit, status, log, diff
2. **Remote & GitHub** — push, pull, clone, remote
3. **.gitignore** — hiding sensitive files, virtual environments, API keys
4. **Branching** — create, switch, work on features safely
5. **Merging** — combine branches, resolve conflicts
6. **Pull Requests** — team collaboration on GitHub
7. **Undoing Mistakes** — reset, stash, revert

## Files
| File | Purpose |
|------|---------|
| `day4_git_github.py` | Runnable reference guide — all Git commands explained |
| `day4_exercises.py` | Hands-on exercises to practice in the terminal |
| `feature.py` | Created during Exercise 4 (branching practice) |

## Key Commands

### The Daily Workflow
```bash
git status                    # Check what changed
git add days/day4/            # Stage specific folder
git commit -m "description"   # Save with message
git push                      # Upload to GitHub
```

### Branching Workflow
```bash
git checkout -b feature-name  # Create & switch to branch
# ... make changes, add, commit ...
git checkout main             # Switch back
git merge feature-name        # Merge feature into main
git branch -d feature-name    # Delete branch
```

### Pull Request Workflow
```bash
git checkout -b feature-name  # Create branch
# ... make changes, add, commit ...
git push origin feature-name  # Push branch to GitHub
# → Go to GitHub → Create Pull Request → Merge
git checkout main && git pull # Sync locally
```

## AI Engineering Connection
- **Branching**: Test new AI models without breaking production
- **.gitignore**: Protect API keys (OpenAI, Gemini) from being exposed
- **Pull Requests**: Code review before deploying AI features
- **Version control**: Track experiments, rollback bad model configs

# Git Cheat Sheet

## Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Core Workflow
```bash
git init                  # initialise repo
git clone <url>           # clone remote repo
git status                # show working tree status
git add <file>            # stage file
git add .                 # stage all changes
git commit -m "message"   # commit staged changes
git push origin main      # push to remote
git pull                  # fetch + merge
```

## Branching
```bash
git branch <name>         # create branch
git switch <name>         # switch to branch
git switch -c <name>      # create + switch
git merge <name>          # merge branch into current
git branch -d <name>      # delete branch
```

## Inspection
```bash
git log --oneline         # compact commit history
git diff                  # unstaged changes
git diff --staged         # staged changes
git blame <file>          # who changed what line
```

## Undo
```bash
git restore <file>        # discard working-tree changes
git restore --staged <f>  # unstage
git revert <commit>       # new commit that undoes a commit
git reset --soft HEAD~1   # undo last commit, keep changes staged
```

## Remotes
```bash
git remote -v             # list remotes
git remote add origin <url>
git fetch origin          # download without merging
```

# Git Commands for Version Control

# Step 1: Initialize Git repository
git init

# Step 2: Check status of files
git status

# Step 3: Add files to staging area
git add .
# Or add specific file: git add app.py

# Step 4: Commit files with message
git commit -m "Initial commit: Backend API"

# Step 5: Create a new repository on GitHub
# Go to https://github.com -> New Repository
# Copy the remote URL

# Step 6: Add remote origin
git remote add origin https://github.com/yourusername/your-repo.git

# Step 7: Push code to GitHub
git push -u origin main

# Additional useful commands:
git log --oneline          # View commit history
git branch -M main        # Rename branch to main
git status                # See modified files
git diff                  # See changes in files
git add <filename>        # Stage specific file
git commit -m "message"   # Commit with message
git push                  # Push commits to remote
git pull                  # Pull latest from remote

				     ROS2 Day 6

## Topic
Repository Cleanup and Documentation

## Objectives
- Clean ROS2 repository
- Learn why build/install/log folders should not be uploaded
- Improve README
- Organize project structure

## Concepts Learned

### .gitignore
Used to ignore files and folders that should not be uploaded to GitHub.

### build/
Generated automatically by colcon build.

### install/
Contains installed executables after building.

### log/
Stores build logs.

### src/
Contains the actual ROS2 source code and packages.

## Commands Used

git status

git add

git commit

git push

git pull --rebase

git rm -r --cached

## Interview Points

Why should build/, install/, and log/ not be uploaded?

Because they are automatically generated files.
Only the source code inside src/ should be stored in GitHub.

What is .gitignore?

It tells Git which files or folders should not be tracked.

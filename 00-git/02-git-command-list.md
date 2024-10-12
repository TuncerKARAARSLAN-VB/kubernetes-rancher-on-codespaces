# Git Command List

Here’s a table of essential Git commands along with their descriptions:

| **Command**               | **Description**                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| `git init`                | Initializes a new Git repository in the current directory.                                                 |
| `git clone <repo-url>`    | Clones an existing repository from a remote server (like GitHub) to your local machine.                    |
| `git add <file>`          | Adds a specific file to the staging area.                                                                  |
| `git add .`               | Adds all changes (new, modified, deleted files) in the current directory to the staging area.              |
| `git commit -m "message"` | Commits staged changes with a message describing the changes.                                              |
| `git status`              | Displays the status of the working directory and staging area, showing tracked/untracked changes.          |
| `git log`                 | Displays the commit history for the current branch.                                                        |
| `git diff`                | Shows the differences between the working directory and the last commit.                                   |
| `git branch`              | Lists all branches in the repository.                                                                      |
| `git branch <branch-name>`| Creates a new branch.                                                                                      |
| `git checkout <branch>`   | Switches to the specified branch.                                                                          |
| `git merge <branch>`      | Merges the specified branch into the current branch.                                                       |
| `git pull`                | Fetches and merges changes from the remote repository to the current branch.                               |
| `git push`                | Pushes committed changes from the local repository to the remote repository.                               |
| `git fetch`               | Downloads changes from the remote repository but doesn’t apply them to the working directory.              |
| `git reset`               | Resets the current HEAD to a specific state, modifying the index and optionally the working directory.      |
| `git revert <commit>`     | Reverts a commit by creating a new commit that undoes the changes from the specified commit.               |
| `git rm <file>`           | Removes a file from the working directory and stages the removal for the next commit.                      |
| `git stash`               | Temporarily saves changes that aren’t ready to be committed, allowing you to work on other things.         |
| `git stash pop`           | Applies the most recent stashed changes back to the working directory and removes them from the stash list.|
| `git tag <tag-name>`      | Creates a tag (reference) for a specific commit, often used for releases.                                  |
| `git remote -v`           | Displays the URLs of the remote repositories linked to your local repository.                              |
| `git show <commit>`       | Displays information about a specific commit, including changes made in the commit.                        |
| `git config --global user.name "name"`  | Sets the global username for Git commits. |
| `git config --global user.email "email"` | Sets the global email for Git commits. |

This table covers the most commonly used Git commands, helping you navigate through version control tasks efficiently.
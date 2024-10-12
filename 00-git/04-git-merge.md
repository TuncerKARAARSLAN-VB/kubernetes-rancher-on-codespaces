# Git Merge

The `git merge` command in Git is used to combine two branches into one. It integrates changes from one branch (usually a feature branch) into another branch (typically the `main` or `develop` branch). Merging is a key part of Git’s branching and collaboration workflow, allowing multiple developers to work on the same project concurrently.

## Types of Merges in Git

1. **Fast-Forward Merge**:
   - If there is a linear path between the branch being merged and the current branch (meaning no new commits have been made to the current branch since the feature branch diverged), Git will perform a **fast-forward merge**.
   - This simply moves the branch pointer forward, incorporating the changes without creating a merge commit.

2. **Three-Way Merge**:
   - If there is no linear history (i.e., if both branches have diverged and have their own separate commits), Git will perform a **three-way merge**.
   - A **merge commit** will be created to combine the changes from both branches.

3. **Conflict**:
   - If the same lines of code have been changed in both branches, a **merge conflict** occurs. Git will pause the merge process, allowing you to manually resolve the conflicts before completing the merge.

---

## Basic `git merge` Command

1. **Merging Branches**:
   To merge another branch into your current branch, first, switch to the branch you want to merge changes into, and then run the merge command.

   Example:

   ```bash
   git checkout main  # Switch to the branch you want to merge into
   git merge feature-branch  # Merge the 'feature-branch' into 'main'
   ```

   This will merge the `feature-branch` into the current `main` branch.

2. **Fast-Forward Merge**:
   If there are no new commits in the `main` branch since `feature-branch` diverged, Git will perform a fast-forward merge. The history will be linear, and no extra merge commit will be created.

   ```bash
   git checkout main
   git merge feature-branch
   ```

3. **Three-Way Merge**:
   If both branches have diverged, Git will perform a three-way merge, where changes from both branches are combined into a new merge commit.

   ```bash
   git checkout main
   git merge feature-branch
   ```

   After this, a merge commit will be created with a message like "Merge branch 'feature-branch' into main."

---

## Merge Conflicts

- When merging branches, if the same file is modified in both branches, a **merge conflict** may occur.
- Git will indicate which files are in conflict and mark the areas of conflict within the files.
- You need to manually resolve the conflict by editing the file, choosing which changes to keep (or combining both), and marking it as resolved.

### Resolving Conflicts

1. Open the file marked with a conflict and you will see conflict markers like:

   ```text
   <<<<<<< HEAD
   Changes from the current branch (main)
   =======
   Changes from the branch being merged (feature-branch)
   >>>>>>> feature-branch
   ```

2. Edit the file to keep the desired changes and remove the conflict markers.

3. After resolving conflicts, mark the file as resolved:

   ```bash
   git add <file>
   ```

4. Complete the merge with:

   ```bash
   git commit  # This commits the merge with a merge commit message
   ```

---

## Additional Merge Options

- **`--no-ff`**:
  - By default, Git will perform a fast-forward merge if possible. To force a merge commit even when a fast-forward is possible, use the `--no-ff` option.

  Example:

  ```bash
  git merge --no-ff feature-branch
  ```

  This ensures that a merge commit is always created, which helps in maintaining a clear history of merges.

- **`--squash`**:
  - The `--squash` option allows you to combine all changes from the branch being merged into a single commit, but without actually performing a merge. This is useful when you want to retain a cleaner commit history.

  Example:

  ```bash
  git merge --squash feature-branch
  git commit -m "Squashed changes from feature-branch"
  ```

  This doesn't create a merge commit but applies all the changes from the `feature-branch` into a single commit.

- **`--abort`**:
  - If a merge goes wrong, or if you don't want to continue with the merge, you can abort the merge process and return to the state before the merge started using the `--abort` option.

  Example:

  ```bash
  git merge --abort
  ```

  This is useful if you run into conflicts and decide not to continue with the merge.

---

## Summary of `git merge`

- **Fast-Forward Merge**: A simple merge where Git moves the branch pointer forward.
- **Three-Way Merge**: A merge that creates a new commit to combine changes from both branches.
- **Merge Conflicts**: Occurs when both branches modify the same file, requiring manual resolution.
- **Merge Options**:
  - `--no-ff`: Forces a merge commit, even if fast-forward is possible.
  - `--squash`: Combines changes into a single commit, without creating a merge commit.
  - `--abort`: Aborts the merge process and reverts to the state before the merge started.

By mastering `git merge`, you can confidently integrate changes between branches, manage conflicts, and maintain a clean Git history.

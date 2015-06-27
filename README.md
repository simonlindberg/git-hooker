# git-hooker
Manage multiple git hooks at once

`git-hooker` is able to find and invoke multiple git hooks.
Running two or more git hooks is not possible without some modification,
either you merge them or chain them.

This solution chains the git hooks by looking for scripts with the request git hooks name in the folders inside of `.git/hooks/`.

So if you have two groups of incompatible git hooks, the `hooks` folder would look like this:

````
hooks
 ├── README.md
 ├── applypatch-msg -> git-hooker.py
 ├── commit-msg -> git-hooker.py
 ├── post-applypatch -> git-hooker.py
 ├── post-checkout -> git-hooker.py
 ├── post-commit -> git-hooker.py
 ├── post-merge -> git-hooker.py
 ├── post-receive -> git-hooker.py
 ├── post-rewrite -> git-hooker.py
 ├── post-update -> git-hooker.py
 ├── pre-applypatch -> git-hooker.py
 ├── pre-auto-gc -> git-hooker.py
 ├── pre-commit -> git-hooker.py
 ├── pre-push -> git-hooker.py
 ├── pre-rebase -> git-hooker.py
 ├── pre-receive -> git-hooker.py
 ├── prepare-commit-msg -> git-hooker.py
 ├── push-to-checkout -> git-hooker.py
 ├── update -> git-hooker.py
 ├── git-hooker.py
 └── some-checks
 |      ├── pre-rebase
 |      ├── prepare-commit-msg
 |      └── commit-msg
 └── other-hooks
        ├── prepare-commit-msg
        ├── pre-push
        └── post-rewrite

````

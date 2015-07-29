#!/usr/bin/env python

import sys
import os
import subprocess

# The first part of the input is the path to the script
full_hook_path = sys.argv[0]

# The rest of the input is the parameters
arguments = " ".join(sys.argv[1:])

script_split = full_hook_path.split("/")

# The last part of the script path is the name of the hook to be run
hook = script_split[-1]

# The rest is the directory where it resides
hook_dir = "/".join(script_split[0:-1])

# The roots are all the directories in the hook directory,
# here we will search for actual git hooks
roots = next(os.walk(hook_dir, followlinks=True))[1]

# Sort to have a guaranteed order
roots = sorted(roots)

git_command = os.popen("ps -ocommand= -p " + str(os.getppid())).read()
os.environ["GIT_COMMAND"] = git_command

# Search the roots for scripts with the same name as the hook and
# run it with the given arguments
for root in roots:
  for current_dir, _, files in os.walk(hook_dir + '/' + root, followlinks=True):
    if current_dir.count(".git") > 1:
      continue
    for f in files:
      path = current_dir + "/" + f
      if f == hook and os.path.isfile(path) and os.access(path, os.X_OK):
        exit_code = os.system(path + " " + arguments)
        if exit_code != 0:
          del os.environ["GIT_COMMAND"]
          sys.exit(exit_code)

del os.environ["GIT_COMMAND"]

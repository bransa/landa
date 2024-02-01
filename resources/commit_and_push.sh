#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <branch_name> <commit_message>"
  exit 1
fi

branch_name="$1"
commit_message="$2"

check_changes() {
  if [ -z "$(git status --porcelain)" ]; then
    echo "No changes to commit."
    exit 0
  fi
}

commit_and_push() {
  git add .
  git commit -m "$commit_message"
  git push origin "$branch_name"
}

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: Current directory is not a Git repository."
  exit 1
fi

git checkout "$branch_name"


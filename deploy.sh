#!/usr/bin/env sh

git pull
git add .
echo commit message
read varname
git commit -m "$varname"
git push --all

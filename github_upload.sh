#!/bin/bash

echo Enter a commit comment

read commitComment

git add -A
git commit -m "$commitComment"
git push

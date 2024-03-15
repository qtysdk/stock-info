#!/usr/bin/env bash
LIST=$(git tag | sort -V | head -1)

for release in $LIST
do
  echo $release
  git tag -d $release
  git push origin :$release
done

#!/bin/sh

if [[ $(git status -s) ]]
then
    echo "The working directory is dirty. Please commit any pending changes."
    exit 1;
fi

git push origin src

echo "Deleting old publication"
rm -rf public
mkdir public

echo "Generating site"
hugo --gc --minify


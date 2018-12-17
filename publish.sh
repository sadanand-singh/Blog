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

# transfer
scp -P 2222 -r public/2014 public/2015 public/404.html public/FibonacciNumbers public/PalakPaneer public/PrimeNumberAndPath public/RplotsFacebbok public/archives public/authors public/categories public/css public/favicon.ico public/index.html public/index.json public/js public/post public/posts public/project public/sitemap.xml public/tags  datascl2@162.241.224.119:~/public_html/


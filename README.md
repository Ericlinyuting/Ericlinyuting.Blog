# YTLinTaiwan.github.io

pelican -r -l

# How to publish to github
pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages  
git push https://github.com/Ericlinyuting/ytlintaiwan.github.io.git gh-pages:master

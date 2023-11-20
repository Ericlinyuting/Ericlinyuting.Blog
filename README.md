# YTLinTaiwan.github.io

# How to publish to github
pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages  
git push https://github.com/Ericlinyuting/ytlintaiwan.github.com.git gh-pages:master
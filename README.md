# YTLinTaiwan.github.io

# dependency package
pip freeze > requirements.txt
pip install -r requirements.txt

# Conda Environment
conda env export > environment.yml

# run project
pelican -r -l

# How to publish to github
pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages  
git push https://github.com/Ericlinyuting/Ericlinyuting.Blog.git gh-pages:master

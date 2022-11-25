### github_commiter



## Installation
``` bash
pip install -r requirements.txt
```


## usage
* clone the project
* open new repository
* run the following commands at the init step 
``` bash
echo "# github_commits" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<Username>/<Repository_Name>.git
git push -u origin main
```

* run the python script [main.py]

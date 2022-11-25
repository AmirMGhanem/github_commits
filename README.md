# github_commiter :) 😁
### using GitPython and Yaml Libraries 🎸


## Installation ➕
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


## if you want to push manually 😅
### use the command below
``` bash
 git commit --date="21 nov 2021" -m "Your commit message"
```



### Linux

I will be using `crontab`.

1.  Open crontab with: `sudo crontab -e`
2.  Add the following line: `59 23 * * * cd /path/to/script/folder/ ; /usr/bin/env /usr/local/bin/python3.8 /path/to/script/main.py`
3.  Thats it! Make sure you save and exit.

Note. There may be git config issues, I solved them by generating a GitHub token in the developer settings. Using the github token as a login for git, make sure git is logged in your system.

Additional information about [crontab](https://crontab.guru)

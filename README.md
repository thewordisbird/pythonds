# pythonds 
https://runestone.academy/runestone/books/published/pythonds/index.html

Online book covering data structures and algorithms in python.

## Setup On New Device
When working through this book on a new device, the following steps will set up the enviornment with the most recent version of the repository.
1. Clone repository to parent folder (desktop/devel):
code `git clone https://github.com/JustinHBird/pythonds.git`

2. Create virtualenv in repository folder:
code `$vitrualenv venv`

3. Activate virtualenv:
code `./venv/scripts/activate`

4. Install requierments:
code `pip install -r requierments.txt`

## Update Remote Repository
After working in the local repository, it is important to update the remote repository to keep everthing up to date.
Notes: If any librarys are added via pip create a new requierments.txt file:
code `pip freeze > requierments.txt`

1. Check git status to see what files were modified and if all should be committed. Any that shouldn't should be added to the .gitignore file.
code `git status`

2. Add files to local repository use code `--all` to add all files:
code `git add [file]`

3. Commit files to local repository:
code `git commit -m "descriptive message"`

4. Commit files to remote repository:
code `git push origin master`

## Update Local Repository
When using a different device the local repository should be updated before moving forward
1. Download the remote repository history:
code `git fetch`

2. Check the status to see differences:
code `git status`

3. If everything looks ok, pull the remote version down to the local device:
code `git pull`

3. If the requierments.txt file has been updated run:
code `pip install -r requierments.txt
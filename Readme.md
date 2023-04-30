# End To End ML Project Implementation

### Day 1
1 : Create Environment
```
conda create -p venv python==3.8 -y
```
2 : Set up the github repository
```
git init
git add Readme.md
git commit -m "Readme commit"
git branch -M main
git remote add origin https://github.com/Sahiljosan/ML_Project4_End_To_End.git
git remote -v
git config --global user.name "Sahil Josan"
git config --global user.email sahiljosan50@gmail.com
git push -u origin main 
```
3 : Create .gitignore file in repository <br>
pull .gitignore file in vs code 
```
git pull
```
4 : Create setup.py file and requirement.txt file in vs code 

5 : Create src(source) directory and create __init__.py file in it

6 : Write code in setup.py and install requirements.txt
```
pip install -r requirements.txt
```
- After this we get mlproject.egg-info, in which we have different different packages


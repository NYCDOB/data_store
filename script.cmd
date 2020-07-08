cd C:\Users\tahsi\uploadingFolder

git pull https://github.com/NYCDOB/data_store.git

del Phase_1_Site_Inspections_2.csv

git add Phase_1_Site_Inspections_2.csv 

git commit -m "delete from script"

 

python automation.py

git branch master

git checkout -f master

git status

git add Phase_1_Site_Inspections_2.csv 

git commit -m "commit from script"

git push --set-upstream https://NYCDOB:showeR%%Pea2@github.com/NYCDOB/data_store.git
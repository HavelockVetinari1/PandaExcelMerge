# PandaExcelMerge
Code for union-ing two or more Excel files under one. The tool essentially takes the contents of two Excel files and smushes them under one file. Note that it's assuming that the data inside them was exported from just one source and all of the columns match across both files. I created this to assist with larger Dynamics CRM data migrations and exports.

# Usage
python3 pandas.py "/home/sam/files/InputDirectory" merged_output.xlsx

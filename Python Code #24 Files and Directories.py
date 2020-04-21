# Files and Directories Demo:

from pathlib import Path

path = Path("Hello")

#print(path.mkdir())
#print(path.rmdir())

path = Path()
for file in path.glob("*.py"): # looks for files with .py extension
    print (file)
    
    
print(path.glob("*.xls")) # looks for Excel Files and prints it




import os

# to move file
# source = "08. Moving File\\Source\\file.txt"
# destination = "08. Moving File\\Destination\\file.txt"

# to move folder
source = "08. Moving File\\Source\\folder"
destination = "08. Moving File\\Destination\\folder"

try:
    if os.path.exists(destination):
        print(source + " already exists")
    else:
        os.replace(source, destination)
        print(source + " has been moved")
except FileNotFoundError as e:
    print(e)
    print(source + " was not found")
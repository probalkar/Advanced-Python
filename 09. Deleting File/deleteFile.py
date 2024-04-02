# os.remove() : deletes a file
# os.rmdir() : deletes an empty folder
# shutil.rmtree() : deletes a non-empty folder

import os
import shutil

file = "09. Deleting File\\file.txt"
empty_folder = "09. Deleting File\\empty folder"
non_empty_folder = "09. Deleting File\\non empty folder"

try:
    os.remove(file)
    os.rmdir(empty_folder)
    shutil.rmtree(non_empty_folder) # dangerous!!
except FileNotFoundError:
    print("That file doesn't exist")
except PermissionError:
    print("You don't have permission to delete that")
except OSError:
    print("You can't delete that using that function")
else:
    print("File/Folder deleted successfully!")
import os

file = "D:\\Python OOP\\04. File Detection\\sample.txt"
folder = "D:\\Python OOP\\04. File Detection\\folder"

paths = [file, folder]

for path in paths:
    if os.path.exists(path):
        print("That location exists!")
        if os.path.isfile(path):
            print("That is a file!")
        elif os.path.isdir(path):
            print("That is a folder!")
    else:
        print("That location doesn't exist!")
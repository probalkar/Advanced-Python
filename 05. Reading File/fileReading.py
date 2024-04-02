try:
    with open("05. Reading File\\sample.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("File not found :(")
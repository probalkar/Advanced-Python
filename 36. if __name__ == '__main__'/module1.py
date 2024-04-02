def hello():
    print("Hello from module1.py")

if __name__ == "__main__":
    print("module1.py is being run directly")
    hello()
else:
    print("module1.py is being imported into another module")
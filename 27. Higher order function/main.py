# higher order function : function that takes another function as an argument or returns a function as a result

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello, world!")
    print(text)

hello(loud)
hello(quiet)
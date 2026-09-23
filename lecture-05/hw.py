def format_strings(*args):
    alltext = "".join(args)
    spaced = alltext.split()
    result = "-".join(spaced).upper()
    print(result)
    pass

if __name__ == '__main__':
    result = format_strings("Helo", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"

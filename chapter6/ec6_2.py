while True:
    i  = input("Enter text(enter-exit) : ")
    if i == "":
        break
    elif i.isalpha():
        print("Text is alphabetic")
    elif i.isalnum():
        print("Text is alpha and numeric")
    elif i.isspace():
        print("Text is string")

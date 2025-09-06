def num_to_text(num):
    text = ""
    for i in num:
        if i == "0":
            text += "Zero "
        if i == "1":
            text += "One "
        if i == "2":
            text += "Two "
        if i == "3":
            text += "Three "
        if i == "4":
            text += "Four "
        if i == "5":
            text += "Five "
        if i == "6":
            text += "Six "
        if i == "7":
            text += "Seven "
        if i == "8":
            text += "Eight "
        if i == "9":
            text += "Nine "
    
    print(text)

num = input("Enter your num : ")
num_to_text(num)
def num_to_text(num):
    text = ""
    for i in num:
        if i == "0":
            text = text + "Zero "
        elif i == "1":
            text += "One "
        elif i == "2":
            text += "Two "
        elif i == "3":
            text += "Three "
        elif i == "4":
            text += "Four "
        elif i == "5":
            text += "Five "
        elif i == "6":
            text += "Six "
        elif i == "7":
            text += "Seven "
        elif i == "8":
            text += "Eight "
        elif i == "9":
            text += "Nine "
    print(text)    


i = input("Enter your num : ")
num_to_text(i)
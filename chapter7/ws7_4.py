import math
def select_menu():
    menu = "=========\n | Menu | \n=========\n"
    menu += "1. Circle\n2. Rectangle\n3. Exit\nPlease choose : "
    choice = input(menu)
    return(choice)

def cal_circle(radius):
    area = math.pi*radius*radius
    return area

def cal_rectangle(width,height):
    area = width*height
    return(area)

print("Program calculate area.")
choice = ''
while choice != '3':
    choice = select_menu()
    if choice == "1":
        radius = float(input("Enter radius : "))
        print("Area of circle = %7.3f"%cal_circle(radius))
    elif choice == "2":
        width = float(input("Enter width : "))
        height = float(input("Enter height : "))
        print("Area of rectangle = %7.3f"%cal_rectangle(width,height))
    elif choice == "3":
        print("Exit Program.")
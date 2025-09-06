# Program name : exam05_08.py

price = 12_345.00
qty = int(input("Enter quantity product : "))

total = price * qty 
print("\nTotal Price : ",format(total,',.2f'))
print(f"\nTotal Price : {total:,.2f}")
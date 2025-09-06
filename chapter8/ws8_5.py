def check_rate(total):
    rates =  [0.10,0.075,0.05,0.025,0.0]
    total_sales = [20000.0,10000.0,5000.0,1000,1.0]
    for n in range(len(total_sales)):
        if total < total_sales[n]:
            return(rates[n])

def get_sale():
    sales = []
    count = 1
    done = True
    while done:
        sale = float(input(f"Enter sale {count} (-1 to exit) : "))
        if sale > -1.0:
            sales  += [sale]
            count += 1
        elif sale == -1.0:
            done = False
    return(sales)
    
sales = get_sale()
total =  sum(sales)
rate = check_rate(total)
commision = total * rate

print(f"Total sales : {total:.2f}")
print(f"Commision Rate : {rate*100:.2f}%")
print(f"Total Commision : {commision:.2f}%")
def check_rate(total):
    rates = (0.10,0.075,0.05,0.025,0.0)
    total_sales = (20000,10000,5000,1000,1.0)
    for n in range(len(total_sales)):
        if total > total_sales[n]:
            return(rates[n])

def get_sale():
    global sales
    for n in range(1,8):
        sale = float(input(f"Enter sale day {n} : "))
        sales += (sale,)

def sum_sale():
    total = 0
    for n in range(len(sales)):
        total += sales[n]
    return(total)

def report():
    print(f"\nTotal sale : {total_sale:.2f}")
    print(f"Commision rate : {rate*100:.2f}%")
    print(f"Total Commision : {commision:.2f}")

sales = ()
get_sale()
total_sale = sum_sale()
rate = check_rate(total_sale)
commision = total_sale * rate
report()
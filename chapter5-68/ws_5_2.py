# 6806021610182 ณัฐวัตร จิตอารี

num1 = int(input("Enter value number1 : "))
num2 = int(input("Enter value number2 : "))
num3 = int(input("Enter value number3 : "))
MinValue = min(num1,num2,num3)
MaxValue = max(num1,num2,num3)

print()
print("Your enter number : ",num1,num2,num3)
print("Maximum value : ",MaxValue)
print("Minimum value : ",MinValue)
print("Average value : ", round(sum((num1,num2,num3))/3,2))
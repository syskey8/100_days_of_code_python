import math

principal = 0
rate = 0
time = 0

principal = int(input("Enter the principal amount: "))
while principal <= 0:
    principal = int(input("Invalid amount. Enter pricipal amount again: "))

rate = int(input("Enter the rate percentage: "))
while rate <= 0:
    rate = int(input("Invalid percentage enter rate percentage: "))

time = int(input("Enter the no. of years: "))
while time <= 0:
    time = int(input("Invalid time entered. Enter no. of years again: "))

amount = principal * pow((1 + rate / 100), time)

print(f"Final amount that will be received: {amount:.2f}")
print(f"Total Profit: {amount - principal:.2f}")
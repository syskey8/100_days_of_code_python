foods = []
prices = []
total = 0

while True:
    food = input(print("Enter your food item or press q to quit: "))
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {food} : $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end = ' ') # replaces the endline with " "

for price in prices:
    total += price

print(f"Your total is : ${price}")


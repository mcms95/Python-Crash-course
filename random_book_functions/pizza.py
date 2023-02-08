pizza = {
    'crust': 'thin',
    'toppings': ['bacon', 'extra cheese'],
}

# summarize the order
print(
    f"Hello you order a pizza with {pizza['crust']} crust, with the folling toppings: ")

for topping in pizza['toppings']:
    print(f"{topping.title()}")

# arbitrary arguments come always on last
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza(12, 'shrooms')
make_pizza(24, 'tuna', 'shrooms', 'letuce')

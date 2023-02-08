house = ["red", "green", "blue"]
print(house)
print(house[1].title())
print(house[-1].title())
print(f"my favorite color is {house[-1].upper()}")
print("\n")

# how to change n value on list - just acess their location and change value
house = ["red", "green", "blue"]
print(house)
house[0] = "black"
print(house)
print("\n")

# to append elements on the list just use append() (add to the end)
house.append("orange")
print(house)
print("\n")

# to insert in n positio we use insert(position, value)
house.insert(0, "yellow")
print(house)
print("\n")

# to remove elements we use del
del house[0]
print(house)
print("\n")

# use pop method to delete but still can use some value
popped_color = house.pop(3)
print(f"my favorite color is {popped_color.title()}")
print(house)
print("\n")

# remove by value using remove('value')
house.remove('black')
print(house)
print("\n")

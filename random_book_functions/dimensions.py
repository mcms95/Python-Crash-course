# type tuple
# dimensions = (200,)
# print(type(dimensions))

# type int
# dimensions = (200)
# print(type(dimensions))

dimensions = (200, 50)
for dimension in dimensions:
    print(f"Original {dimension} dimensions")
print("\n")
dimensions = (250, 40)
for dimension in dimensions:
    print(f"Changed {dimension} dimensions")

# range() function generate numbers / stops on final number not included
for value in range(1, 5):
    print(value)

# using range to create a list
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# list to print square numbers from 1 to 10
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# simple statistics with numbers
digits = list(range(0, 10))
print(f"This is a list of {digits}")
print(min(digits))
print(max(digits))
print(sum(digits))

# one line square list
ss = [value**2 for value in range(1, 11)]
print(ss)

responses = {}
pool_active = True

while pool_active:
    name = input("Whats your name? ")
    response = input("Whats your favorite country? ")

    responses[name] = response

    repeat = input("Would you like to add someone else? yes/no")
    if repeat == 'no':
        pool_active = False

print("---Pool results: ---")
for name, response in responses.items():
    print(f"\n{name.title()} favorite country is {response.title()}")

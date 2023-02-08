def build_person(first_name, last_name, age=""):
    person = f"{first_name} {last_name}"
    if age:
        person['age'] = age
    return person


while True:
    print("\nPlease tell me your first name: ")
    first = input("First name: ")
    last = input("Last name: ")
    final = build_person(first, last)
    print(f"\nGreetings {final}!")

# musician = build_person('nuno', 'silva')

confirmed_users = []
unconfirmed_users = ['nuno', 'joana', 'didi']

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Checking {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users are confirmed:")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()} ")

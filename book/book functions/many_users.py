users = {
    'nsilva': {
        'nome': 'nuno',
        'apelido': 'silva',
        'cidade': 'parede'
    },

    'jsoares': {
        'nome': 'joana',
        'apelido': 'soares',
        'cidade': 'sassoeiros'
    },
}

for username, user_info in users.items():
    print(f"User {username}:")
    full_name = f"{user_info['nome']} {user_info['apelido']}"
    location = f"{user_info['cidade']}"

    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}\n")

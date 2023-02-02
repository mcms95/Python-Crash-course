def build_profile(first, last, **userinfo):
    userinfo['first_name'] = first
    userinfo['last_name'] = last
    return userinfo


person = build_profile('nuno', 'silva',
                       location='parede',
                       job='croupier',
                       favorite_color='orange')
print(person)

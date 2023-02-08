fav_language = {
    'nuno': ['python', 'c', 'aws'],
    'nina': ['c'],
    'tomas': ['python', 'java', 'php'],
    'didi': ['java']
}
# print(f"Didi's fav language is {fav_language['didi'].title()}")
# new = fav_language.get('nuno', 'sorry not vailable')
# old = fav_language.get('rebeca', 'sorry not vailable')
# print(new)
# print(old)
# people = ['nuno', 'nina', 'joao', 'filipe']

# loop to print names and language with special message for those in people too
for name, languages in fav_language.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        if len(languages) == 1:
            print(f"\t{language.title()}")
        else:
            print(f"\t{language.upper()}")

#    if name in people:
#        print(f"{name.title()} you know {language.title()} a great language!")

# a set eleminates the duplicates
# print("\nThe programing languages refred are:")
# for language in set(fav_language.values()):
#    print(f"{language.title()}")

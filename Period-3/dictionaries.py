favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'jen':'rust'
}
# dictionaries are made of keys and values
# the key jen has a value of python
print(favorite_languages)
print(f"Jen's favorite language is {favorite_languages['jen']}")
favorite_languages['jen'] = 'javascript'
print(f"Jen's favorite language is {favorite_languages['jen']}")
# if you have a duplicate key, only the last one is used
# but the order doesn't change. 

# print dictionaries the Pythonic way

# to print keys and values the template is
# for key,value in dictionary_name.items()

for person,language in favorite_languages.items():
    print(f"The favorite language of {person.title()} is {language.title()}")

# to print keys only the template is
# for key in dictionary_name.keys()

for person in favorite_languages.keys():
    print(person.title())
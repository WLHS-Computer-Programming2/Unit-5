favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'jen':'rust'
}
# dictionaries are made of keys and values
# the key jen has a value of python

print(f"Jen's favorite language is {favorite_languages['jen']}")

# if you have a duplicate key, only the last one is valid
# modifying values in dictionary

favorite_languages['sarah'] = 'c++'
for key in favorite_languages:
    print(f"The favorite language of {key} is {favorite_languages[key]}")

# the order of keys is preserved - note jen is still first even though
# there was a second dictionary value for jen
print("\n")
# remove a key-value pair
del favorite_languages['phil']
for key in favorite_languages:
    print(f"The favorite language of {key} is {favorite_languages[key]}")
print("\n")

# you can use pop if you want to store the value - key is not stored
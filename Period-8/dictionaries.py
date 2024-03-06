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

# what if I try to retrieve a key that doesn't exist?
# [] leads to a KeyValue exception, .get() returns None
# print(favorite_languages['smith'])
print(favorite_languages.get('smith'))
print(favorite_languages.get('edward'))


### Activity ###
# 1) Make a dictionary of the favorite colors of each person in the class

# 2) Write a function called reverse_lookup that will take in a color and dictionary and
# return a list of each person with that favorite color
favorite_colors = {
    'tristan':'red',
    'colton':'blue',
    'meri':'red',
    'aron':'black',
    'cardin':'blue',
    'neil':'green',
    'ajay':'blue',
    'spencer':'red',
    'kevin':'purple',
    'aaron':'green',
    'vincent':'purple',
    'cole':'blue',
    'eli':'navy',
    'matthew':'purple',
    'nick':'black',
    'alex': 'orange'
}

def reverse_lookup(fav_colors:dict,color:str)->list:
    '''Searches a dictionary for anyone with a particular
    favorite color
    
    Parameters
    ----------
    fav_colors - a dictionary of people and their favorite colors
    
    color - the favorite color we are looking for
    
    Return
    ------
    A list of the people whose favorite color is color'''
    list_of_people = []
    for person in fav_colors:
        if(fav_colors[person] == color):
            list_of_people.append(person)
    return list_of_people


color = 'purple'
new_line = "\n"
print(f"The following people have a favorite color of {color}:\n{new_line.join(reverse_lookup(favorite_colors,color))}")
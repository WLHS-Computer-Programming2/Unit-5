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
    'aaron':'black',
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

temp = ['adam','bob','cam','don']
print("\n".join(temp).title())
color = 'purple'
new_line = "\n"
print(f"The following people have a favorite color of {color}:\n{new_line.join(reverse_lookup(favorite_colors,color)).title()}")

# Looping through dictionaries

# by key-value pairs
#    key   value
for person,color in favorite_colors.items():
    print(f"{person.title()}'s favorite color is {color.lower()}.")

for person,test_data in quizzes.item():
    for test, score in test_data.item():
        
# by values
color_string = ""
for color in set(favorite_colors.values()): # set removes dups
    color_string += f"{color.lower()}, "

color_string = color_string[:-2]+"."
print(f"The colors mentioned were: {color_string}")

# by keys
student_string = ""
for student in sorted(favorite_colors.keys()): # sorted will alphabetize
    student_string += f"{student.title()}, "
student_string = student_string[:-2]
print(f"The students are: {student_string}.")

# Nesting info with dictionaries
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

#   dict name  key          key
print(users['aeinstein']['location'])
print(users['mcurie']['first'].title())
print(users['aeinstein'])
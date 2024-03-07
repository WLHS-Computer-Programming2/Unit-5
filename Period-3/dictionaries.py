favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    "jen": "rust",
}
# dictionaries are made of keys and values
# the key jen has a value of python
print(favorite_languages)
print(f"Jen's favorite language is {favorite_languages['jen']}")
favorite_languages["jen"] = "javascript"
print(f"Jen's favorite language is {favorite_languages['jen']}")
# if you have a duplicate key, only the last one is used
# but the order doesn't change.

# print dictionaries the Pythonic way

# to print keys and values the template is
# for key,value in dictionary_name.items()

for person, language in favorite_languages.items():
    print(f"The favorite language of {person.title()} is {language.title()}")

# to print keys only the template is
# for key in dictionary_name.keys()

for person in favorite_languages.keys():
    print(person.title())

# to print only the values the template is
# for value in dictionary_name.values()

print(f"The following languages have been favorited: ")
for language in favorite_languages.values():
    print(language.title())

# to print in alphabetical order, used sorted()
for person in sorted(favorite_languages.keys()):
    print(f"{person.title()}, thank you for taking the survey.")

favorite_languages["eden"] = "ruby"
print(favorite_languages)

# print unique values use set()
print("The following languages were mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

"""Task: Make a dictionary of the favorite colors of
each person in the room. Print all people and their
fav color, nicely formatted. Then print a list of 
the colors that were mentioned, no duplicates. Lastly,
print a list of first names in alphabetical order,
nicely formatted.
Extension: Print out how many times each color was mentioned."""
favorite_colors = {
    "Ronin": "Green",
    "Finley": "Blue",
    "Alex": "Mint",
    "Ryan": "Blue",
    "Parker": "Orange",
    "Toby": "Red",
    "Eden": "Red",
    "Lucas": "Blue",
    "Logan": "Purple",
    "Garrett": "Red",
    "Luke": "Blue",
    "Ayana": "Blue",
    "Drew": "Navy",
    "Tristan": "Pink",
}

for person,color in favorite_colors.items():
    print(f"{person.title()}'s favorite color is {color.lower()}.")

print("The colors mentioned were: ",end="")
color_string = ""
for color in set(favorite_colors.values()):
    color_string += f"{color.lower()}, "

color_string = color_string[:-2]+"."
print(color_string)

print("The students are: ",end="")
student_string=""
for student in sorted(favorite_colors.keys()):
    student_string += f"{student}, "
student_string = student_string[:-2]+"."
print(student_string)
users = {
    'aeinstein':{
        'first name':'albert',
        'last name':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first name':'marie',
        'last name':'curie',
        'location':'paris'
    },
    'rfeynman':{
        'first name':'richard',
        'last name': 'feyman',
        'location': 'cal tech'
    }
}
#   key       value(dict)
for username,user_info in users.items():
    print(f"The user with username {username} has a:")
    #   key  value
    for info,value in user_info.items():
        print(f"\t{info} of {value.title()}")
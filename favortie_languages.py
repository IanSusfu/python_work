favorite_languags = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languags.keys():
    print(name.title())
    if name in friends:
        print('Hi ' + name.title()+ ', I see your favorite language is ' + favorite_languags[name].title() + '!' )



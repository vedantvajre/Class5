favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
people = ['jen', 'edward', 'Bobby', 'Kate']

for name in people:
    if name in favorite_languages:
        print("Thank you for responding!")
    else:
        print("Please respond to my poll!")
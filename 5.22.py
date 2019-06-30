name_prompt = "\nWhat is your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat == 'yes':
        break

print("\n-- Results --")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
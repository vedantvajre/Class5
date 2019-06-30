prompt = "How many people are you reserving today?"
prompt += "\n(Type quit to close)"

for number in range(1, 25):
    number = input(prompt)
    if number > str(8):
        print("Because you have quite a few people, you will have to wait for a table. Sorry for the inconvenience.")
    elif number == 'quit':
        break
    else:
        print("Your table is ready!")
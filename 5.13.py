prompt = "If you were to choose a Honda, Acura, Toyota, or Mazda, which one would you choose?"
prompt += "\n(Type quit to close)"

car = ['Honda', 'Acura', 'Toyota', 'Mazda']
while True:
    cars = input(prompt)
    if cars.title() in car:
        print("let me see if I can find you a(n) " + cars)
    elif cars == "quit":
        break
    else:
        print("Please choose a car from the list!")
        continue

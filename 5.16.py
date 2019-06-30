prompt = "Please enter in pizza toppings: "
prompt += "\n(Type quit to stop)"

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("I will add " + topping + " to your pizza.")

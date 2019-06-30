sandwich_orders = [
    'cheese', 'veggie', 'pastrami', 'turkey',
    'pastrami', 'ham', 'pastrami']
finished_sandwiches = []

print("Unfortunately, we're all out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
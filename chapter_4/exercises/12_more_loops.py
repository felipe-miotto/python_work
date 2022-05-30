pizzas = ['portuguesa', 'peperonni', 'burrata']
friends_pizzas = pizzas[:]

pizzas.append('banana')
friends_pizzas.append('calabresa')

print("My favorite pizzas are:")
for pizzas in pizzas:
    print(pizzas.title())

print("\nMy friend's favorites pizzas are:")
for pizzas in friends_pizzas:
    print(pizzas.title())

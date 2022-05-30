pizzas = ['portuguesa', 'peperonni', 'burrata']
friends_pizzas = pizzas[:]

pizzas.append('banana')
friends_pizzas.append('calabresa')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorites pizzas are:")
for pizza in friends_pizzas:
    print(f"- {pizza}")

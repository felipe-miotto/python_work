my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

# This doesn't work:
# my_foods = friends_foods

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

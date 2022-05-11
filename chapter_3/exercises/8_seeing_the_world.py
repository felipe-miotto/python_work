places = ['NY', 'Dubai', 'Ibiza', 'Japan', 'Germany']
print(f"Original list: \n{places}")
print(f"\nAlphabetically: \n{sorted(places)}")
print(f"\nNow back to normal: \n{places}")

places.reverse()
print(f"\nReverse now: \n{places}")

places.reverse()
print(f"\nReverse again, so original order: \n{places}")

print("\nFriendly reminder, from now on, all of the functions are permanent!")
places.sort()
print(f"\nTrying sort function: \n{places}")

places.sort(reverse=True)
print(f"\nTrying sort function, but reversed: \n{places}")

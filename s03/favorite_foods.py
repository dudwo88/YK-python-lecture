myFavouritFood = ['pizza', 'sushi', 'tacos', 'ramen', 'burger']

print('=== My Favourite Foods ===')
print(f'Original: {myFavouritFood}')

print()
print(f'Reversed: {myFavouritFood[::-1]}')

print()
sortedList = sorted(myFavouritFood)
print(f'Alphabetical: {sortedList}')

print()
hasSushi = "sushi" in myFavouritFood
hasKimchi = "kimchi" in myFavouritFood

print(f"Is 'sushi' in the list? {hasSushi}")
print(f"Is ''kimchi' ' in the list? {hasKimchi}")

print()
myFavouritFood.append('kimchi')
print(f"After adding 'kimchi': {myFavouritFood}")

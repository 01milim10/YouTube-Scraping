# A list is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get a length
print(len(fruits))

# Append to a list
fruits.append('Mangoes')

# Remove from a list
fruits.remove('Grapes')

# Inster into position
fruits.insert(2, 'Strawberries')

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Change value
fruits[0] = 'Blueberries'

print(fruits)

# Reverse sort
fruits.sort(reverse=True)

print(fruits)


print(numbers, numbers2)

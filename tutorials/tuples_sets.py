# A Tuple is a collection which is orderd and unchangeable. ALlows duplicate members.

# Create Tuple
fruits = ('Apples', 'Organges', 'Grapes')
fruits2 = tuple(('Apples', 'Organges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get a value
print(fruits[1])

# Cant change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# A set is a collection which is unordered and unindexed. No duplicate members
fruits_set = {'Apples', "Oranges", ' Mangoes'}

# Check if is set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Add duplicate
fruits_set.add('Apples')

# Remove from set
fruits_set.remove('Grapes')

# Clear set
fruits_set.clear()

# Delete Set
del fruits_set

# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
person2 = dict(first_name='Sarra', last_name='Williams')

print(person, type(person))
print(person2, type(person2))

# Get value
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dictionaries keys
print(person.keys())

# Get dictionaries items
print(person.items())

# Copy Dictionaries
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del (person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print((len(person2))) 

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[0]['name'])

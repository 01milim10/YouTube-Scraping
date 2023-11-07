name = 'Brad'
age = 27

# String Formatting

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings
# print(f"Hello, my name is {name} and I am {age}")


# String Methods
s = 'hello world'

# Captitalize strings
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap Case
print(s.swapcase())

# Get Length
print(len(s))

# Replace
print(s.replace("world", "everyone"))

# Count
sub = 'h'
print(s.count(sub))

# Starts With
print(s.startswith('hello'))

# Ends With
print(s.endswith('d'))

# Spllits into a list
print(s.split())

# Find a postion
print(s.find('r'))

# Find all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

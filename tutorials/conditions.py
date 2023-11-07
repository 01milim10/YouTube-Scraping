# If/Else conditions are use to decide to do something based on something being true or false.

x = 10
y = 10


# Comparison Operators (==, !=, >, <, >=, <=) - use to compare two values.

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else

# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# elif
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{y} is greater than {x}')

# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than 10')

# Logical Operators (and, or, not) - used to combine conditional statements.
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# Membership Operators (not, not in, in, is, is not) - used to check if a value is present in an object

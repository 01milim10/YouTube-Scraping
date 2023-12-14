##While Loop
## A while loop is used to execute a block of statements repeatedly until a given condition is satisfied. 
## And when the condition becomes false, the line immediately after the loop in the program is executed.

##Syntax
## while expression:
##    statement(s)

##Example
count = 0
while (count < 3): 
    count = count + 1
    print("Hello World") 

## For Loop
##For loops are used for sequential traversal. For example: traversing a list or string or array etc. 

## Syntax:
## for iterator_var in sequence:
##    statements(s)

##Example
fruits = ['Apple', 'Banana', 'Pineapple', 'Mangoes', 'Peach', 'Strawberry']
for fruit in fruits:
    print(fruit)
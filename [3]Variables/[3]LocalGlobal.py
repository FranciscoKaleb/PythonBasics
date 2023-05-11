#[1]
print('-----------------[1]------------------')
dummy_name = 'stephen'

def greet(str):
    name = str
    return 'Hello ' + name

print(greet('kaleb'))

# print(name) , would cause error because we are trying to access a variable in a function
print(dummy_name)

#[2]
print('-----------------[2]------------------')
def accessVariableOutside():
    print(dummy_name)

accessVariableOutside()

#[3] reassigning value to a variable outside the function TURNS the variable local
print('-----------------[3]------------------')
def modifyVariableOutside():
    dummy_name = 'Curry' # the variable dummy_name is different from the outside dummy_name
    print(dummy_name)

modifyVariableOutside()
print(dummy_name)

#[4] would cause error
print('-----------------[4]------------------')
def modifyVariableOutside():
    print(dummy_name)
    dummy_name = 'Curry'

# modifyVariableOutside() would cause error

#[5] SOLUTION to number 4
print('-----------------[5]------------------')
def modifyVariableOutside():
    global dummy_name # reference to the outside dummy_name, will not create a local variable
    print(dummy_name)
    dummy_name = 'Curry' # changes the outside dummy_name's value

modifyVariableOutside()

print(dummy_name)
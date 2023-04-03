# methods

#[1] upper()
x = "Hello World"
print(x.upper()) # doesnt change x, has a return value so it needs assignment '='
print(x)
x = x.upper()
print(x)

#[2] lower() 
x = x.lower()
print(x)
x = "Hi this is a string"
print(x)

#[3] split() returns a list
x = x.split() # split on white space by default, removes white space
              # x is now a list after split
print(x)


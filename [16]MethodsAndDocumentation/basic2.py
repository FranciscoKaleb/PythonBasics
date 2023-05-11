#[14] *args, returns a tuple
print('-----------------[14]------------------')


def myfunc(a,b,c,d):
    return sum((a,b,c,d)) * .05

print(myfunc(70,30,100,100))


def myfunc2(*args):
    return sum((args))

print(myfunc2(2,3,4))

#[15] **kwargs, return a dictionary
print('-----------------[15]------------------')
def mufunc2(**kwargs): 
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

mufunc2(fruit = 'Dorian')

#[16] using *args and **kwargs at the same time
print('-----------------[16]------------------')

def myFunc3(*args, **kwargss):
    print(args)
    print(kwargss)
    print('I would like {} {}.'.format(args[1],kwargss['fruit']))

myFunc3(0,1,2,fruit = 'banana', fruit2 = 'apple')

#[17] exercise
print('-----------------[17]------------------')
def myfunc(*args):
    temp = []
    for num in args:
        if num%2 == 0:
            temp.append(num)
    return temp

print(myfunc(1,2,3,4,5))

#[18] exercise
print('-----------------[18]------------------')
def myfunc(str1):
    new_str = ''
    str1_len = len(str1)
    for num in range(0,str1_len):
        if num%2 == 0:
            new_str = new_str + str1[num].upper()
        else:
            new_str = new_str + str1[num].lower()
    return new_str

print(myfunc('The rat corpse is smelly'))

#[19] exercise, returns lesser if both num is even, returns greater if both is odd
print('-----------------[19]------------------')
def myFunc(num1, num2):
    if num1%2 == 0 and num2%2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    elif num1%2 != 0 and num2%2 != 0:
        if num1 > num2:
            return num1
        else:
            return num2
    else:
        pass

print(myFunc(3,5))
print(myFunc(2,4))
print(myFunc(2,5))

#[20] exercise, returns true if both word starts with the same letter
print('-----------------[20]------------------')
def myFunc(str1, str2):
    if str1[0].startswith(str2[0]):
        return True
    else:
        if str1[0].upper() == str2[0].upper():
            return 'Same letter but different case'

    
print(myFunc('Kaleb', 'kite'))
print(myFunc('dog', 'dart'))

#[21]
print('-----------------[21]------------------')
def capitalizeFirstAndFourth(str1):
    new_str = ''
    for num in range(0,len(str1)):
        if num == 0:
            new_str = new_str + str1[num].upper()
        elif num == 3:
            new_str = new_str + str1[num].upper()   
        else:
            new_str = new_str + str1[num]
    return new_str

print(capitalizeFirstAndFourth('kaleb'))

#[22]
print('-----------------[22]------------------')
def reverseString(str1):
    new_str = str1[::-1]
    return new_str

print(reverseString('kaleb'))

#[23] counting occurence using find() --- counting the number of times a given pattern appears in a string, including overlap
print('-----------------[23]------------------')

str1 = 'hahahah'
str_to_find = 'aha'
str_len = len(str_to_find)
index_list = []
str_index = 0
current_index = 0


while str_index != -1:
    str_index = str1.find(str_to_find, current_index)
    current_index = str_index + str_len -1
    if str_index != -1:
        index_list.append(str_index)

print(f"substring '{str_to_find}' found in index {index_list}")

#[24] multiplying string challenge
print('-----------------[23]------------------')
str1 = 'hello'
new_str = ''

for char in str1:
    new_str = new_str + char*3

print(new_str)

#[25] write a function that takes in a list of integers and returns true if it contains 007 in order
print('-----------------[24]------------------')
# function that accepts a list then combines it and returns a string
def listToString(my_list):
    new_list = []
    new_str = ' '

    for num in range(0, len(my_list)):
        new_list.append(str(my_list[num]))
    
    return new_str.join(new_list)

# function that accepts a list and find a specific substring, returns true if it is found and false if not
def spyGame(my_list):

    if listToString(my_list).find('0 0 7') != -1:
        return True
    else: 
        return False

print(spyGame([1,2,3,4,5,0,0,7]))
print(spyGame([1,2,3,4,5,0,7])) 
    
#[26] return a list of prime numbers that exist up to the given max primeNumbers(max)
print('-----------------[25]------------------')
# function that return the number of prime number that exist up to and including a given number
count = 0
prime = 0
def primeNumber(max):
    global count, prime
    prime = 0

    for num in range(2, max + 1):
        for n in range(num, 1, -1):
            # print(n, end = '')
            if num%n == 0:
                count = count + 1
            if count > 1:
                break
        if count == 1:
            prime = prime + 1
        count = 0
        # print('')
    return prime



print(primeNumber(97))
print(primeNumber(1000)) # takes less than a second to calculate
#print(primeNumber(10000)) # takes like 3 seconds to calculate
#print(primeNumber(100000)) # it takes like 3 minutes to calculate this

#[26] map() applying function in each member of a list using map(function, list)
print('-----------------[26]------------------')

def square(num):
    return num**2
my_list = [4,5,6]
#---------------
for mem in map(square, range(0,3)):
    print(mem, end = ' ')
print('')
#----------------
for mem in map(square, [1,2,6]):
    print(mem, end = ' ')
print('')
#----------------
for mem in map(square, my_list):
    print(mem, end = ' ')
print('')
#----------------
print(list(map(square,[4,9,8])))
print(list(map(lambda num: num**2,[2,3,4])))
print(list(map(lambda name: name[0],['Sally', 'Dali', 'Kaleb'])))








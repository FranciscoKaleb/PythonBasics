# methods

#[1] upper() - turns all letters in string to upper case
print('-----------------[1 - upper() ]------------------')
x = "Hello World"
print(x.upper()) # doesnt change x, has a return value so it needs assignment '='
print(x)
x = x.upper()
print(x)

#[2] lower() or casefold() - turns letters to lower case; 
print('-----------------[2 - lower() ]------------------')
x = x.lower()
print(x)
x = "ßHi this is a string"
print(x)
x = x.casefold() #converts 'ß' to 'ss'
print(x)

#[3] split() returns a list data type which is like an equivalent of a container in c++
print('-----------------[3 - split() ]------------------')
x = x.split() # split on white space by default, removes white space
              # x is now a list after split
print(x)

#[4] changing matched word in a string method 1
# has its own specific uses like for example you want to change all the 'an' word in a sentence without affecting
# those words with 'an' in their parts like the word animal, ban, man, tan etc...
# only affecting the 'an' in the phrase 'an apple'
print('-----------------[4 - ]------------------')
myStr2 = 'The dog in the doghood is my friend.\n'\
         'My neighbor always feed the dog with snaks'
print(myStr2)

tempList = myStr2.split() #deletes backslash characters and splits by space
print(tempList)

index_count = 0

while index_count < len(tempList):
    
    if tempList[index_count] == 'dog':
        tempList[index_count] = 'cat'
    else:
        pass
    index_count += 1

print(tempList)
myStr2 = ''
for mem in tempList:
    myStr2 = myStr2 + mem + ' '

print(myStr2)

#[5] replace() changing matched word in a string using replace() method 2
print('-----------------[5 - replace() ]------------------')
myStr2 = 'The dogin the neighborhood is my friend.\n'\
         'My neighbor always feed the dog with snaks'

myStr3 = myStr2.replace('dog', 'alligator')
print(myStr3)

#[6] split between \n 
print('-----------------[6 - split() ]------------------')

newList = myStr2.split('\n')
print(newList)

#[7] count() counting the occurence of a substring/letter count('substr', start, end)
print('-----------------[7 - count() ]------------------')
myStr2 = 'The dogin the neighborhood is my friend.\n'\
         'My neighbor always feed the dog with snaks'
print(myStr2.count('o'))


#[8] capitalize()  
# converts the first character of a string to an uppercase letter and all other alphabets to lowercase.
#capitalizing the beginning of the sentences
print('-----------------[8 - capitalize() ]------------------')
myStr3 = 'the doctor was not present yesterday. i was suppose to have my check up that day'

myList = myStr3.split('. ')
print(myList)

index_count = 0

while index_count < len(myList):
    myList[index_count] = myList[index_count].capitalize()
    index_count += 1

print(myList)

#[9] center(width, ' ') --> used to put padding character in the start and end of a string
# 1 split the string between \n
# 2 count the length of every string in the list created from split, put it in another list
# 3 find the max in the list that contain the length of every string from split()
# 4 put the max value as the width parameter of center()
print('-----------------[9 - center() ]------------------')
myStr4 = 'Hello I am Kaleb\n'\
         'I am from Calo\n'\
         'dog'
print(myStr4)
    # 1
myList = myStr4.split('\n')
print('')
print(f'myList {myList}')
print(' ')

index_count = 0
index_len = 0
List_len = [None] * len(myList)

    # 2
while index_count < len(myList):
    index_len = len(myList[index_count])
    List_len[index_count] = index_len
    index_count += 1
    #List
print(List_len)

    # 3
max_len = max(List_len)
print(f'{max_len} is max')

    # 4
print(' ')
print('centralized string. . . .')

index_count = 0

while index_count < len(myList):
    myList[index_count] = myList[index_count].center(max_len, ' ')
    index_count += 1

for mem in myList:
    print(mem)

#[10] endswith() method returns True if a string ends with the specified suffix. 
print('-----------------[10 - endswith() ]------------------')
message = 'Python is fun'

# check if the message ends with fun - returns a boolean
print(message.endswith('fun'))

#[11]  expandtabs() method returns a copy of string with all tab characters
# '\t' replaced with whitespace characters until the next multiple of tabsize parameter.
print('-----------------[11 - expandtabs() ]------------------')
str = 'xyz\t12345\tabc'

print(str)

result = str.expandtabs(1) #default is 8 spaces if no argument

print(result)

#[12] encode() method returns an encoded version of the given string.
print('-----------------[12 - encode() ]------------------')

title = 'Python Programming'

# change encoding to utf-8
print(title.encode())

#[13] find()  method returns the index of first occurrence of the substring (if found). 
# If not found, it returns -1.
print('-----------------[13 - find() ]------------------')
str3 = 'the dog is a big dog. I like that dog'
print(str3.find('dog'))


#[14] index() method returns the index of a substring inside the string (if found).
#  If the substring is not found, it raises an exception.
print('-----------------[14 - index() ]------------------')
text = 'Python is fun'

# find the index of is
result = text.index('is')
print(result)
# Output: 7
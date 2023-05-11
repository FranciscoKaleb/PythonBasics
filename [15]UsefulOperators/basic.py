

#[1] range()
print('-----------------[1]------------------')
myList = [1,2,3,4,5]

for mem in range(10):
    print(mem) #prints 0 - 9

# range(start , end)
print('-----------------[2]------------------')
for mem in range(3,10):
    print(mem) #prints 3 - 9

# range(start , end , steps)
print('-----------------[3]------------------')
for mem in range(2,20,3):
    print(mem)

# using range to act like a c for loop
print('-----------------[3]------------------')
myList = ['cow', 'cat', 'dog', 'camel', 'horse']
for i in range(len(myList)):
    print(myList[i])

#[2] casting range() into a list
print('-----------------[4]------------------')
myList2 = list(range(0,20,2))
print(myList2)

#[3] enumerate() - > tuple
print('-----------------[5]------------------')
index_count = 0
word = 'kaleb'

for mem in 'abcde':
    print('At index {}, the letter is {}'.format(index_count, mem))
    index_count += 1

for mem in enumerate(word):
    print(mem) #mem is a tuple pair of index and value

for i, v in enumerate(word):
    print(f'{v} is at index {i}')

#[4] zip() -> tuple
print('-----------------[6]------------------')
myList1 = [1,2,3,4]
myList2 = ['a','b','c','d','e']

for mem in zip(myList1, myList2):
    print(mem) #combine the two list into a tuple

#[5] in keyword
print('-----------------[7]------------------')
myList3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print('s' in myList3)
print('a' in myList3)
print('a' in 'Francisco Kaleb')
print('k2' in {'k1': 1})

#[6] split() refresher
print('-----------------[8]------------------')
str1 = 'the cow is bery hugry'

print(list(str1))
print(str1.split())

#[7] min(list) max(list) shuffle(list)
print('-----------------[9]------------------')
myListOfNum = [11,12, 13,14,5,66,3,12,12,12,12]
print(max(myListOfNum))

#[8] randint(min, max) - directly manipulate passed list. Not returning anything - no return type
print('-----------------[10]------------------')
from random import randint
print(f'{randint(0,1000)} - is a random integer between 0 and 1000')
#[9] count()
print('-----------------[12]------------------')
print(f'the list has {myListOfNum.count(12)} number 12')
#[10] shuffle()
print('-----------------[12]------------------')
from random import shuffle
shuffle(myListOfNum)
print(myListOfNum)
#[11] input , cin equivalent in c++
result = input("Enter a number here:")
print(result)














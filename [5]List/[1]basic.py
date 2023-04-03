#Lists is like the all the c++ containers that can contain any data type

#basics
myList = [1,2,13,4,15,6,7,7,8,9,0]
myList2 = ['String', 100, 23.2]
myList3 = ['one', 'two', 'three']
myList4 = ['five', 'six', 'seven']
lettersList = ['t', 'b', 'c', 's', ]

print(len(myList2)) # outputs 3
print(myList3[0])
print(myList[1:])

#concatenating list
myList5 = myList4 + myList3
print(myList5) 

#changing elements through direct element access
myList3[0] = 'ONE'
print(myList3)

#adding elements in the end using append
myList.append(4)
print(myList)

#removing items from the BACK of the list using pop
myList.pop()
print(myList)

#saving popped items
pop_list = myList.pop()
pop_list = pop_list + myList.pop() # doesnt result into another list but rather an integer
print(f'pop list = {pop_list}')
print(myList)

#removing items using pop(index)
myList5.pop(1)
print(myList5)

#using sort method, has NO return type 
myList.sort()
print(myList)

#will not work because .sort() does not return a type 
newList = myList.sort()
print(newList)
print(f'type of newList is {type(newList)}')
#will work
newList = myList
print(newList)

#reverse sort
newList.reverse()
print(newList)

















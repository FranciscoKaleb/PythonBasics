#[1] Use split() and if to create a statement that will print out words that start with s
print('-----------------[1]------------------')
st = 'print only words that start with s in this sentence'
myList = st.split()
print(myList)

for mem in range(0,len(myList)):
    if myList[mem].startswith('s'):
        print(myList[mem])

#[2]use range to print even numbers from 0-10
print('-----------------[2]------------------')
for num in range(0,11,2):
    print(num)
    
#[3] Use list comprehension between 1 and 50 that are divisible by 3
print('-----------------[3]------------------')
myList2 = [x for x in range(1,50) if(x%3 ==0)]
print(myList2)

#[4] print even if the length of a word in string are even
st = "Print every word in this sentence that has an even number of letters"
print('-----------------[4]------------------')

# 1 split the strings into list of words
myList3 = st.split()

# 2 loop thru every word using for loop or while, 
# 3 then get the len() of every list member each 
# iteration, check in if statement if len is even
print(st)
for mem in myList3:
    if len(mem)%2 == 0:
        print(f"even - '{mem}' has {len(mem)} letters")

#[5] Write a program that prints integers from 1 to 100. But for multiples of three print "Fizz" instead
# of the number. and for the multiples of five print "Buzz". For numbers which are multiples of both 3 and 5
# print "FizzBuzz"
print('-----------------[5]------------------')
for num in range(0,101):
    if num%3 == 0 and num%5 != 0:
        print(f'{num} - Fizz')
    elif num%5 == 0 and num%3 != 0:
        print(f'{num} - Buzzzz')
    elif num%5 == 0 and num%3 == 0:
        print(f'{num} - FizzBuzz')
    else:
        print(num)

#[6] use list comprehension to create a list of the first letters of every word in the string below
print('-----------------[6]------------------')
st = 'Create a list of the first letters of every word in this string'

myList = st.split()
newList = []

for mem in myList:
    newList.append(mem[0])

print(st)
print(newList)


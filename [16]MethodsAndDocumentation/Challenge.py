
#[1] Function that calculates the volume of a sphere given its radius
print('-----------------[1]------------------')
radius = 4.5

def volumeOfSphere(radius):
    import math
    return (4/3)*(math.pi)*(radius**3)

sv = volumeOfSphere(radius)
print(sv)

#[2] function that checks whether a number is in a given range
print('-----------------[2]------------------')
number = 4
def inRange(num, high, low):
    if num <= high and num >= low:
        return True
    else:
        return False
print(inRange(8,7,5))
#[3] function that accepts a string and calculates the number of upper case letters and lower case letters
print('-----------------[3]------------------')
sample_string = 'The butterfly belongs to the State. Boris is bored.'
def countUpperAndLower(string):
    lower = 0
    upper = 0
    for letter in string:
        if letter.islower():
            lower = lower + 1
        elif letter.isupper():
            upper = upper + 1
        else:
            pass
    result = (f'lower case: {lower} \nupper case: {upper}')
    return result
print(countUpperAndLower(sample_string))
#[4] function that takes a list and returns a new list with unique elements of the first list 
print('-----------------[4]------------------')
my_list = ['kaleb', 'kaleb', 'shawarman', 33,33,1,2,3,4,4]
def uniqueInList(mlist):
    return list(set(mlist))
print(uniqueInList(my_list))
#[5] function to multiply all the numbers in a list
print('-----------------[5]------------------')
num_list = [1,2,3,4]
def multiplyListMembers(mlist):
    result = 1
    for num in range(0, len(mlist)):
        result = result*mlist[num]
    return result
print(multiplyListMembers(num_list))
#[6] function that checks whether a passed in string is palindrome or not
print('-----------------[6]------------------')
sample_string = 'ada'
def checkIfPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
print(checkIfPalindrome(sample_string))
#[7] function to check whether a string is pangram or not
#pangram - a string is considered a pangram when all letters from a-z was used at least once
print('-----------------[7]------------------')
sample_string = 'A black Dog eats fruit hours jogging kabar love more nothing pay q wxz'
def isPangram(string):
    a_z = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    for letter in a_z:
        if string.find(letter) > -1:
            pass
        else:
            return False      
    return True
print(isPangram(sample_string))




















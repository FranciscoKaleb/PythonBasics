
# replace symbols with space
def replaceSymbol(myStr):
    myStr = myStr.replace('\n', ' ')
    myStr = myStr.replace('\r', ' ')
    myStr = myStr.replace('\t', ' ')
    myStr = myStr.replace(',', ' ')
    myStr = myStr.replace(':', ' ')
    myStr = myStr.replace(';', ' ')
    myStr = myStr.replace('.', ' ')
    myStr = myStr.replace('?', ' ')
    myStr = myStr.replace('!', ' ')
    return myStr

def strToList(myStr):
    new_list = myStr.split()
    return new_list

import time

#[1] 
print('-----------------[1]------------------')
start_time1 = time.time()
f = open('[10]Files/wikiText1000Lines.txt', 'r', encoding = 'utf-8')  
myStr = f.read()

myStr = replaceSymbol(myStr)
new_list = strToList(myStr)
new_dictionary = {}

# loop through the list and set initial count per key to zero
for mem in new_list:
    new_dictionary.setdefault(mem, 0)

# loop through the same list again and increment key count each time string appear
for mem in new_list:
    new_dictionary[mem] = new_dictionary[mem] + 1

# SORT 1: Alphabetically. sort it alphabetically using key
alphabetically_sorted_list = sorted(new_dictionary)

print('--------sort alphabetically--------')
for mem in alphabetically_sorted_list:
    print(f'{mem} : {new_dictionary[mem]}')

f.close()

end_time1 = time.time()

elapsed_time1 = end_time1 - start_time1
#[2]
print('-----------------[2]------------------')
from collections import Counter
start_time2 = time.time()

ff = open('[10]Files/wikiText1000Lines.txt', 'r', encoding = 'utf-8')  
myStr2 = ff.read()
myStr2 = replaceSymbol(myStr2)
b_dict = Counter(myStr2.split())
b_list = sorted(b_dict)
for mem in b_list:
    print(f'{mem} : {b_dict[mem]}')

ff.close()

end_time2 = time.time()
elapsed_time2 = end_time2 - start_time2

print(f'my written function for unique counter takes {elapsed_time1} seconds')
print(f'built-in function for unique counter takes {elapsed_time2} seconds')
#[3]
print('-----------------[3]------------------')

#[4]
print('-----------------[4]------------------')

#[5]
print('-----------------[5]------------------')

#[6]
print('-----------------[6]------------------')

#[7]
print('-----------------[7]------------------')
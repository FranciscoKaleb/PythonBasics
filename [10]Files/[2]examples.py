
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
    myStr = myStr.replace('"', ' ')
    myStr = myStr.replace('(', ' ')
    myStr = myStr.replace(')', ' ')
    myStr = myStr.replace('*', ' ')
    myStr = myStr.replace('$', ' ')
    myStr = myStr.replace('#', ' ')
    myStr = myStr.replace('/', ' ')
    myStr = myStr.replace('-', ' ')
    return myStr

#[1] creating a function that counts how many times a substring occurs in a text file
# not very reliable way
print('-----------------[1]------------------')
f = open('[10]Files/TextFiles/Bible.txt', 'r')  
temp = f.read()
print(f"the substring 'the' appeared {temp.count(' the ') + temp.count(' The ')} times")
f.close()

#[2] a program that counts how many times each unique word occurs in a text file
print('-----------------[2]------------------')
temp = replaceSymbol(temp)
list_of_words = temp.split(' ')
new_dictionary = {}

for mem in list_of_words:
    new_dictionary.setdefault(mem, 0)

for mem in list_of_words:
    new_dictionary[mem] = new_dictionary[mem] + 1

alphabetically_sorted_list = sorted(new_dictionary)


f = open('[10]Files/BibleWordCountAlphabeticallySorted.txt', 'w')  

for mem in alphabetically_sorted_list:
    print(f'{mem} : {new_dictionary[mem]}')
    f.write(f"{mem} : {new_dictionary[mem]} \n")

f.close()
#[2] writing tuple pairs of unique words in a text file sorted by word count, descending
print('-----------------[2.1]------------------')
f = open('[10]Files/BibleWordCountRankedByCount.txt', 'w')  


list_of_tuple_pair = []
for mem in new_dictionary:
    list_of_tuple_pair.append((mem, new_dictionary[mem]))

print(list_of_tuple_pair)

def take_second(elem):
    return elem[1]

sorted_tuple = sorted(list_of_tuple_pair, key = take_second, reverse = True)

for mem in sorted_tuple:
    print(mem)
    f.write(f"{mem}\n")

f.close()
#[3] replacing a specific word in a text file,  very easy im not doing it
# put in a string
# use .replace method
# rewite the string in the text file
print('-----------------[3]------------------')

#[3.1] sensoring a word in a text file, same logic as the above
print('-----------------[3.1]------------------')

#[4] removing html tags in an html file
print('-----------------[4]------------------')

#[5] alphabetical sorting of words, using sorted() function, already done in the first example
print('-----------------[5]------------------')















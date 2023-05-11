#Dictionaries is the equivalent of unordered map in c++
#it is unordered and cannot be sorted
#it is a key - value pair, key is always a string
#[1]
myDict1 = {'key1':'value1','key2':'value2'}
myDict2 = {'kaleb':26,'Sam':20}
myDict3 = {'Apple':25,'Orange':15, 'Banana':10}
myDict4 = {'k1': 23, 'k2':[1,2,3], 'k3':{'InsideKey':100}}
myDict5 = {'key':['a', 'b', 'c']}

print('-----------------[1]------------------')
print(myDict2['kaleb']) #prints 26
print(myDict3['Banana'])
print(myDict4['k3'])
print(myDict4['k3']['InsideKey'])
print(myDict5['key'][0].upper())
print(myDict5)

#[2]reassigning values
print('-----------------[2]------------------')
myDict5['key'][0] = myDict5['key'][0].upper()
print(myDict5)
myDict2['kaleb'] = 27
print(myDict2)
myDict2['kaleb'] = 'string1'
print(myDict2)

#[3]printing keys and values
print('-----------------[3]------------------')
print(myDict3.keys())
print(myDict3.values())
print(myDict3.items()) # returns a tuple




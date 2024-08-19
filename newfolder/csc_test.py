






import math

#[1] create a list

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []


for num in range(1,51): 
    temp_num = (num/50)*100
    list1.append(temp_num)

for num in range(1,46):
    temp_num = (num/45)*100
    list2.append(temp_num)

for num in range(1,41):
    temp_num = (num/40)*100
    list3.append(temp_num)

for num in range(1,16):
    temp_num = (num/15)*100
    list4.append(temp_num)

new_dict = {}
new_tuple = []
count = 0
for num1 in list1:
    for num2 in list2:
        for num3 in list3:
            for num4 in list4:
                score = math.ceil(((((num1+num2+num3)/3)*0.9)+(num4*0.1))*100)/100
                temp_string = '[' + str(num1) + ' '+ str(num2) + ' ' + str(num3) + ' ' + str(num4) + ']'
                new_dict[temp_string] = score
                list5.append(score)
                count += 1
                
list5.sort()         
for mem in new_dict:
    new_tuple.append((mem,new_dict[mem]))

def take_second(elem):
    return elem[1]

sorted_tuple = sorted(new_tuple, key = take_second, reverse = False)

for (key,value) in sorted_tuple:
    print(f'{key} : {value} ')

print(count)
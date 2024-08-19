


#[1] rounding number
print('-----------------[1]------------------')
import math
value = 4.49
print(math.floor(value))
print(math.ceil(value))
print(round(value))

#[2] pi, e, nan, inf, log
print('-----------------[2]------------------')
print(math.pi)
print(math.e)
print(math.nan)
print(math.inf)
print(math.log(math.e))
print(math.log(100,10)) # 2
#[3] sine
print('-----------------[3]------------------')
print(math.sin(0.5))
print(math.degrees(math.pi/2))
print(math.radians(180))
#[4] random
print('-----------------[4]------------------')
import random
#print(random.seed(1))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
#[5] choose a random index in list
print('-----------------[5]------------------')
my_list = list(range(0,10))
print(my_list)
print(random.choice(my_list))

#[6] choosing a random number without repetition using sample
print('-----------------[6]------------------')
print(random.sample(population=my_list, k = 5))

#[7] random.uniform
print('-----------------[7]------------------')
print(random.uniform(a=0,b=100))


#[8]
print('-----------------[8]------------------')
print(random.gauss(mu=0,sigma=1))
#[9] challenge - loop n times as many as list index. pop a random index in a list, until none is left 
print('-----------------[9]------------------')
new_list = [1,2,3,4,5,6,7,8,9,0,44,13,99,45]
print(new_list)
new_range = len(new_list)-1
randd = 0

for mem in range(len(new_list)-1):
    randd = random.randint(0,new_range-1) # generate random index
    new_list.pop(randd) # pop that index
    print(f'{new_list} {randd} {new_range}') # print the updated list
    new_range = len(new_list) # update the new_range based on new length of the list

#[10] Lotto Algorithm
print('-----------------[10]------------------')
# first part -  generate random combinations of numbers from 1 - 58
    # create a list of int from 1 - 58
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]
combination_list = []
max_count = 6
# select random value from num_list, append that value to a temp_list, do it six times. value must not repeat
print(num_list)
duplicate = True

def check_if_duplicate(temp_list, rand_num):
    for num in temp_list:
        if rand_num == num:
            return True
        else:
            pass

# a function that accepts a list, and a max count, select unique random values from the list and return a list which length is determined by max
def generate_sub_list(num_list, max_count):   
    temp_list = [] 
    while len(temp_list) < max_count:
        rand_num = random.choice(num_list)
        #check if unique before appending, there cant be same number within the 6 number combination
        duplicate = check_if_duplicate(temp_list, rand_num)
        if duplicate == True:
            pass
        else:
            temp_list.append(rand_num)
        duplicate = False # reset bool value to false
    return temp_list

# generating 100 unique 6 digit combinations
for num in range(0, 1000):
    six_list = generate_sub_list(num_list, max_count)
    combination_list.append(six_list)
    six_list = []



# write the combination list in a text file
f = open('[19]Modules/combinations.txt', 'w' , encoding = 'utf-8')

for list in combination_list:
    f.write(str(list) + '\n')

f.close()

# generate 6 digit combination which does not exist in the combination_list AKA the cheat
# its easier to manually check by searching thru the database you own combination

is_unique = False
duplicate_count = 0

while is_unique == False:
    unique_list = generate_sub_list(num_list, max_count)
    for list in combination_list:
        if unique_list == list:
            duplicate_count = duplicate_count + 1
        else:
            pass
    if duplicate_count >= 1:
        is_unique = False
    else:
        is_unique = True
    duplicate_count = 0

print(f'unique - {unique_list}')






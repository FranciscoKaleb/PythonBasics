# while (condition): - runs until condition is true

#[1] while basic incrementing an integer inside while loop
print('-----------------[1]------------------')
x = 0
while x <= 5:
    print(x)
    x = x + 1

#[2] while-else
print('-----------------[2]------------------')
x = 0
while x <= 5:
    print(x)
    x = x + 1
else:
    print(f'{x} is not equal to 5')

#[3] break keyword - stops the loop
print('-----------------[3]------------------')
x = 0
while x <= 5:
    print(x)
    x = x + 1
    if x == 3: #break if x is 3
        break
    

#[4] continue - breaks one iteration of the loop
print('-----------------[4]------------------')
x = 0
while x < 10:
    x = x + 1
    if x%2 == 0: #skips even number
        continue
    else:
        print(x)

#[5] pass keyword - does nothing at all
print('-----------------[5------------------')
for mem in [1,2,3]:
    pass
print('end')







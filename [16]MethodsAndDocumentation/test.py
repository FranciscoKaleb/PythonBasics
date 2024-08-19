def a_func(num):
    if(num == 1 or num == 0):
        return num
    else:
        return a_func(num-1) + a_func(num-2)

print(a_func(2))
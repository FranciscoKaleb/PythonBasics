
#[1] custom, hour minute second microsecond
print('-----------------[1]------------------')
import datetime
my_time = datetime.time(2,20)
my_date = datetime.date(2020, 11, 5)
print(my_time)
print(my_date)
print(my_time.minute)


#[2] getting current date
print('-----------------[2]------------------')
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

#[3] getting current time 
print('-----------------[3]------------------')
now = datetime.datetime.now()
print(now)
print(f'{now.hour}: {now.minute}: {now.second}')

#[4] getting the days between two dates
print('-----------------[4]------------------')

t1 = datetime.date(year = 2018, month = 7, day = 12)
t2 = datetime.date(year = 2017, month = 1, day = 13)

t3 = t1 - t2
print(t3)

t4 = datetime.datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime.datetime(year = 2017, month = 7, day = 12, hour = 8, minute = 7, second = 32)

t6 = t5 - t4
print(t6)

#[5] difference between delta objects
print('-----------------[5]------------------')
t1 = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = datetime.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

t3 = t1 - t2

print("t3 =", t3)


#[6] stop watch
print('-----------------[6]------------------')
import time
counter = 0
print(counter)
counter = counter + 1
time.sleep(1)
print(counter)
counter = counter + 1
time.sleep(1)
print(counter)
counter = counter + 1
time.sleep(1)

#[7] real time ticking
print('-----------------[7]------------------')
import time
bobby = True
while bobby:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)
    bobby = False
#[8] multi threading
print('-----------------[8]------------------')

import threading 
  
def print_hello_three_times():
  for i in range(3):
    print("Hello")
  
def print_hi_three_times(): 
    for i in range(3): 
      print("Hi") 

t1 = threading.Thread(target=print_hello_three_times)  
t2 = threading.Thread(target=print_hi_three_times)  

t1.start()
t2.start()

#[9] multi threading
print('-----------------[9]------------------')

import threading 
import time
  
def print_hello():
  for i in range(4):
    time.sleep(0.5)
    print("Hello")
  
def print_hi(): 
    for i in range(4): 
      time.sleep(0.7)
      print("Hi") 

t1 = threading.Thread(target=print_hello)  
t2 = threading.Thread(target=print_hi)  
t1.start()
t2.start()




























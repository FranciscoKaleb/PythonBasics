

#[1] CREATE AND WRITE; second parameter in open refers to mode:
# w-write(overwrite), 
# a- append in end, 
# r - read, 
# r+ read and write, 
# w+ writing and reading(overwrite)

print('-----------------[1]------------------')
f = open('[10]Files/readmee.txt', 'w')  #if file exist, recreates file
f.write("ming ming")
f.close()

#[2] APPEND mode doesnt recreate the file
print('-----------------[2]------------------')
f = open('[10]Files/readmee.txt', 'a')  
f.write("\n\nming ming")
f.close()

#[3] READ A FILE
print('-----------------[3]------------------')
f = open('[10]Files/readmee.txt', 'r')  
temp = f.read()
print(temp)
f.close()

#[3] READ A FILE MORE THAN ONCE, USE .SEEK() IN A LOOP WHERE YOU NEED TO READ FILE TWICE OR MORE
print('-----------------[4]------------------')
f = open('[10]Files/readmee.txt', 'r')  
temp = f.read()
print(temp)
f.seek(0) 

temp = f.read()
print(temp)
f.close()

#[4] readlines() --  using readlines()
print('-----------------[5]------------------')
f = open('[10]Files/readmee.txt', 'r')  
temp = f.readlines()
print(temp)
f.seek(0)
f.close()

#[5] using with 'open(filepath) as variable_name:' to automatically close a file
print('-----------------[6]------------------')
with open('[10]Files/readmee.txt', 'r') as f_var:
    print(f_var.read())

with open("C:\\Users\\jyuvi\\OneDrive\\Desktop\\Python\\PythonBasics\\newTextFile.txt", 'w') as f_var:
    f_var.writelines('kaleb \nmarquez')

with open("C:\\Users\\jyuvi\\OneDrive\\Desktop\\Python\\PythonBasics\\newTextFile.txt", 'r') as f_var:
    tempstring = f_var.read()
    print(tempstring)






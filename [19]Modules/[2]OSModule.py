


#[1] get current working directory
print('-----------------[1]------------------')
import os
print(os.getcwd())

#[2] list every files in current directory
print('-----------------[2]------------------')
dir_list = os.listdir()
for mem in dir_list:
    print(mem)
#[3] list files in specific directory
print('-----------------[3]------------------')
specific_dir = os.listdir("D:\\downloads\\PythonBasics\\[10]Files\\TextFiles")
for mem in specific_dir:
    print(mem)
#[4] move files using shutil.move(src, destination)
print('-----------------[4]------------------')
import shutil
try:
    shutil.move("D:\\downloads\\PythonBasics\\[10]Files\\TextFiles\\Dummy.txt", "D:\\downloads\\PythonBasics\\[18]OOP\\")
except OSError as error:
    print(error)
#[5] deleting files
print('-----------------[5]------------------')
try:
    os.unlink("D:\\downloads\\PythonBasics\\[10]Files\\TextFiles\\Dummy.txt")
except OSError as error:
    print(error)
#[6] deleting an empty folder
print('-----------------[6]------------------')
try:
    os.rmdir("D:\\downloads\\PythonBasics\\[10]Files\\TextFiless\\")
except OSError as error:
    print(error)
#[7] deleting the folder and every files inside it
print('-----------------[7]------------------')
try:
    shutil.rmtree("D:\\downloads\\PythonBasics\\[10]Files\\newfolderr")
    print('success')
except OSError as error:
    print(error)
#[8] sending files to trash bin using send2trash
print('-----------------[8]------------------')
#ctrl+shift+P ----> Python: select interpreter, choose conda thats where I pip install packages
import send2trash
try:
    send2trash.send2trash("D:\\downloads\\PythonBasics\\[10]Files\\newfolderr")
    print('success')
except OSError as error:
    print(error)


#[9] 'walking' on folders, subdolders, and files
# 1 will list subfolders
# 2 will list files
# 3 will look at first subfolder, list all subfolder and files
# 4 will look at second, third .. subfolder and do the same process like in the first
print('-----------------[9]------------------')
for folder, sub_folders, files in os.walk("D:\\downloads\\PythonBasics\\[19]Modules"):
    print(f'looking at folder: {folder}')
    print('\n')
    print('the subfolders are: \n')
    for sub_fold in sub_folders:
        print(f'\tSubfolder: {sub_fold}')
    print('')
    print('the files are:')
    for f in files:
        print(f'\tFile: {f}')
    print('')
#[10]
print('-----------------[10]------------------')
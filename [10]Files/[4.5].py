



#[1] create an a-z folder
#[2] read xml file
#[3] create a text file for each page, put in respective folder which the name starts with
    # if it see the string '<page>' it should start the function from that line
    # it should copy the first 6 lines in a string, from that copied string we will
    # decide the file name and whether to copy or not the  page into a text file.
    # if next line to <id> is <redirect>, it should SKIP the page. if next to <id> is <revision> save the page
    
    # program should save the substring between the <title> and </title> tag and name the text file to that substr
    # if it see the string '</page>' it should be the last line it will copy
    #then repeat
#[4] delete redirect pages
#[remove tags]


# [1] create an a-z folder
import os
# Get the absolute path of the script
script_path = os.path.realpath(__file__) 
# Get the script directory
script_dir = os.path.dirname(script_path) 
try:
    os.mkdir(f'{script_dir}/newfolder')
    os.mkdir(f'{script_dir}/newfolder/a')
    os.mkdir(f'{script_dir}/newfolder/b')
    os.mkdir(f'{script_dir}/newfolder/c')
    os.mkdir(f'{script_dir}/newfolder/d')
    os.mkdir(f'{script_dir}/newfolder/e')
    os.mkdir(f'{script_dir}/newfolder/f')
    os.mkdir(f'{script_dir}/newfolder/g')
    os.mkdir(f'{script_dir}/newfolder/h')
    os.mkdir(f'{script_dir}/newfolder/i')
    os.mkdir(f'{script_dir}/newfolder/j')
    os.mkdir(f'{script_dir}/newfolder/k')
    os.mkdir(f'{script_dir}/newfolder/l')
    os.mkdir(f'{script_dir}/newfolder/m')
    os.mkdir(f'{script_dir}/newfolder/n')
    os.mkdir(f'{script_dir}/newfolder/o')
    os.mkdir(f'{script_dir}/newfolder/p')
    os.mkdir(f'{script_dir}/newfolder/q')
    os.mkdir(f'{script_dir}/newfolder/r')
    os.mkdir(f'{script_dir}/newfolder/s')
    os.mkdir(f'{script_dir}/newfolder/t')
    os.mkdir(f'{script_dir}/newfolder/u')
    os.mkdir(f'{script_dir}/newfolder/v')
    os.mkdir(f'{script_dir}/newfolder/w')
    os.mkdir(f'{script_dir}/newfolder/x')
    os.mkdir(f'{script_dir}/newfolder/y')
    os.mkdir(f'{script_dir}/newfolder/z')
except OSError as error:
    print('Folder already exist error')

#[2] 
def clean_title(raw_title):
    clean_str = ''
    
    clean_str = raw_title.replace('<title>', '')
    clean_str = clean_str.replace('</title>', '')
    clean_str = clean_str.strip()
    return clean_str

first_letter = ''

def create_path(title):
    global first_letter
    path = ''
    first_letter = title[0].lower()
    path = script_dir + '\\newfolder\\' + first_letter + '\\' + title + '.txt'

    return path


    

line_num = 0
start_line = 0
title = ''
temp_holder = ''

start_copying = False
page_index = -1
end_page_index = -1

page_count = 0
from_start = 0
page_num = 0
revision_found = False
path = ''
revision_found = False
is_file = False

f =  open("[10]Files/TextFiles/wiki.xml", 'r', encoding = 'utf-8')
for line in f:
    line_num = line_num + 1
    # 1
    if start_copying == False:
        page_index = line.find('<page>')
    # 2
    if page_index > -1:
        page_num = page_num + 1
        start_copying = True
        page_index = -1
    # 3
    if start_copying == True:
        from_start = from_start + 1
        if from_start < 5:
            temp_holder = temp_holder + line
            pass
        if from_start == 2:
            title = clean_title(line)
            if title.find('File:') > -1 or title.find('Wikipedia:') > -1: # we dont want to copy File pages
                is_file = True
            else:
                is_file = False 
        if from_start == 5 and line.find('<revision') > -1: # create path when revision is found at line 5
            revision_found = True
            path = create_path(title)
        if from_start >= 5 and revision_found == True:
            temp_holder = temp_holder + line
            pass
        else:
            pass 
        end_page_index = line.find('</page>')
    # 4
    if revision_found == True and end_page_index > -1 and is_file == False: # this new version is way faster than the 
        #revious one that uses append mode, it will just write to file if it doesnt found the </page> string
        try:
            with open(path, 'w', encoding = 'utf-8') as f:
                f.write(temp_holder)
        except OSError as error:
            try:
                os.mkdir(f"{script_dir}\\newfolder\\{first_letter}")
                with open(f"{script_dir}\\newfolder\\{first_letter}\\{title}.txt", 'w', encoding = 'utf-8') as f:
                    f.write(temp_holder)
            except OSError as error: 
                try:
                    os.mkdir(f"{script_dir}\\newfolder\\{first_letter}(1)")
                    with open(f"{script_dir}\\newfolder\\{first_letter}({title})\\{title}.txt", 'w', encoding = 'utf-8') as f:
                        f.write(temp_holder)
                except OSError as error: 
                    print(f'{title} - I guess we can print this crap')    
            print(f'{title} folder already exist')
        #NEED TO IMPROVE CLEANING TITLE BECAUSE SOME CHAR ARE NOT ALLOWED IN FILENAME
    #  5
    if end_page_index > -1: # I could just put this code on the if statement at the top tbh
        start_copying = False
        revision_found = False
        end_page_index = -1
        from_start = 0
        temp_holder = ''
        title = ''
        path = ''
    # 6
    if line_num%1000000 == 0:
        print(line_num)
f.close()   


string_holder = ''

#f = open('the big xml')
#for line in f:
#    pass
#f.close()

def writeToText():
    pass













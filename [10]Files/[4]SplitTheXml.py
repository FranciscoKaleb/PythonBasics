



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

def create_path(title):
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
part1 = ''
part2 = ''
part3 = ''
part4 = ''
part5 = ''
part6 = ''
part7 = ''
part8 = ''
part9 = ''
part10 = ''
part11 = ''
part12 = ''
part13 = ''
part14 = ''
part15 = ''
f =  open("[10]Files/TextFiles/wiki.xml", 'r', encoding = 'utf-8')
for line in f:
    line_num = line_num + 1

    if start_copying == False:
        page_index = line.find('<page>')

    if page_index > -1:
        page_num = page_num + 1
        start_copying = True
        page_index = -1
        
    
    if start_copying == True:
    
        from_start = from_start + 1

        if from_start < 5:
            #temp_holder = temp_holder + line
            pass
        
        if from_start == 2:
            title = clean_title(line)
            
        if from_start == 5 and line.find('<revision') > -1: # create path when revision is found at line 5
            revision_found = True
            #path = create_path(title)

        if from_start >= 5 and revision_found == True:
            #temp_holder = temp_holder + line
            pass
        else:
            pass 

        end_page_index = line.find('</page>')

    
    if revision_found == True and end_page_index > -1: # this new version is way faster than the 
        # previous one that uses append mode, it will just write to file if it doesnt found the </page> string
        #print(f"[{page_num}] [revision] '{title}' page found at line {line_num}")
        if line_num > 0 and line_num < 100000000:
            part1 = part1 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 100000000 and line_num < 200000000:
            part2 = part2 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 200000000 and line_num < 300000000:
            part3 = part3 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 300000000 and line_num < 400000000:
            part4 = part4 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 400000000 and line_num < 500000000:
            part5 = part5 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 500000000 and line_num < 600000000:
            part6 = part6 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 600000000 and line_num < 700000000:
            part7 = part7 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 700000000 and line_num < 800000000:
            part8 = part8 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 800000000 and line_num < 900000000:
            part9 = part9 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 900000000 and line_num < 1000000000:
            part10 = part10 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 1000000000 and line_num < 1100000000:
            part11 = part11 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 1100000000 and line_num < 1200000000:
            part12 = part12 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 1200000000 and line_num < 1300000000:
            part13 = part13 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 1300000000 and line_num < 1400000000:
            part14 = part14 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        if line_num > 1400000000 and line_num < 1500000000:
            part15 = part15 + (f"[{page_num}] [revision] '{title}' page found at line {line_num}\n")
        

        #try:
            #with open(path, 'w', encoding = 'utf-8') as f:
                #f.write(temp_holder)
                #pass
        #except OSError as error:
            #print('Folder already exist error')
    
    if revision_found == False and end_page_index > -1:
        #print(f"[{page_num}] [redirect] '{title}' page found at line {line_num}")
        #all_title = all_title + (f"[{page_num}] [redirect] '{title}' page found at line {line_num}\n")
        #print('')
        pass
        
    if end_page_index > -1:
        start_copying = False
        revision_found = False
        end_page_index = -1
        from_start = 0
        #temp_holder = ''
        title = ''
        #path = ''
    if line_num%5000000 == 0:
            print(line_num)
    if line_num == 100000000:
        with open('[10]Files/part1.txt', 'w', encoding = 'utf-8') as f:
            f.write(part1)
    if line_num == 200000000:
        with open('[10]Files/part2.txt', 'w', encoding = 'utf-8') as f:
            f.write(part2)
    if line_num == 300000000:
        with open('[10]Files/part3.txt', 'w', encoding = 'utf-8') as f:
            f.write(part3)
    if line_num == 400000000:
        with open('[10]Files/part4.txt', 'w', encoding = 'utf-8') as f:
            f.write(part4)
    if line_num == 500000000:
        with open('[10]Files/part5.txt', 'w', encoding = 'utf-8') as f:
            f.write(part5)
    if line_num == 600000000:
        with open('[10]Files/part6.txt', 'w', encoding = 'utf-8') as f:
            f.write(part6)
    if line_num == 700000000:
        with open('[10]Files/part7.txt', 'w', encoding = 'utf-8') as f:
            f.write(part7)
    if line_num == 800000000:
        with open('[10]Files/part8.txt', 'w', encoding = 'utf-8') as f:
            f.write(part8)
    if line_num == 900000000:
        with open('[10]Files/part9.txt', 'w', encoding = 'utf-8') as f:
            f.write(part9)
    if line_num == 1000000000:
        with open('[10]Files/part10.txt', 'w', encoding = 'utf-8') as f:
            f.write(part10)
    if line_num == 1100000000:
        with open('[10]Files/part11.txt', 'w', encoding = 'utf-8') as f:
            f.write(part11)
    if line_num == 1200000000:
        with open('[10]Files/part12.txt', 'w', encoding = 'utf-8') as f:
            f.write(part12)
    if line_num == 1300000000:
        with open('[10]Files/part13.txt', 'w', encoding = 'utf-8') as f:
            f.write(part13)
    if line_num == 1400000000:
        with open('[10]Files/part14.txt', 'w', encoding = 'utf-8') as f:
            f.write(part14)
f.close()   

with open('[10]Files/part15.txt', 'w', encoding = 'utf-8') as f:
    f.write(part15)
print(page_num)
string_holder = ''

#f = open('the big xml')
#for line in f:
#    pass
#f.close()

def writeToText():
    pass













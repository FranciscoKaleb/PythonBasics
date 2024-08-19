import random
my_list = [20, 15, 13, 47, 39, 24]
list_of_matches_line_number = []

line_count = 0
matched_line_number = 0

with open("[19]Modules/combinations.txt", 'r', encoding = 'utf-8') as fileobject:
    for line in fileobject:
        line_count = line_count + 1
        #print(f'[{line_count}] {line}')
        if line.find(str(my_list)) != -1:
            print('match')
            matched_line_number = line_count
            list_of_matches_line_number.append(matched_line_number)

if (len(list_of_matches_line_number) >= 1):
    for num in list_of_matches_line_number:
        print(f'match at line number {num}')
else:
    print('theres no match')

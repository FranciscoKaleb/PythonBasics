#[1] 
print('-----------------[1]------------------')
import re
string = 'the landline number of the company is 817-113-7420 or 888-740-1219'
pattern = "(\d\d\d-\d\d\d-\d\d\d\d)"
for match in re.finditer(pattern, string):
    print(f'at {match.span()} : {match.group()} ')

# \d+ one or more occurence
# \d{3} exactly three occurence
# \d{2,3} 2 or 3 occurence


#[2]
print('-----------------[2]------------------')
import re
string = 'the landline number of the company is 817-113-7420 or 888-740-1219'
pattern = r'(\d{3})-(\d{3})-(\d{4})'
for match in re.finditer(pattern, string):
    print(f'at {match.span()} : {match.group()} ')
#[3]
print('-----------------[3]------------------')

#[4]
print('-----------------[4]------------------')

#[5]
print('-----------------[5]------------------')

#[6]
print('-----------------[6]------------------')

#[7]
print('-----------------[7]------------------')
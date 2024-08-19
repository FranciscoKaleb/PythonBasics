

# [] - Square brackets - Square brackets specifies a set of characters you wish to match.

# [abc]	    a	        1 match
#           ac	        2 matches
#           Hey Jude	No match
#           abc de ca	5 matches

# [a-e] is the same as [abcde]
# [1-4] is the same as [1234]
# [0-39] is the same as [01239]
# [^abc] means any character except a or b or c.
# [^0-9] means any non-digit character.



# . - Period - A period matches any single character (except newline '\n').

#   ..	    a	    No match
#           ac	    1 match
#           acd	    1 match
#           acde	2 matches (contains 4 characters)



# ^ - Caret - The caret symbol ^ is used to check if a string starts with a certain character.

#   ^a	    a	    1 match
#           abc	    1 match
#           bac	    No match


# $ - Dollar - The dollar symbol $ is used to check if a string ends with a certain character.

#   a$	    a	        1 match
#           formula	    1 match
#           cab	        No match


# * - Star - The star symbol * matches ZERO or more occurrences of the pattern left to it.

#   ma*n	mn	    1 match
#           man	    1 match
#           maaan	1 match
#           main	No match (a is not followed by n)
#           woman	1 match


# + - Plus The plus symbol + matches ONE or more occurrences of the pattern left to it.

#   ma+n	mn	    No match (no a character)
#           man	    1 match
#           maaan	1 match
#           main	No match (a is not followed by n)
#           woman	1 match


# ? - Question Mark - The question mark symbol ? matches zero or one occurrence of the pattern left to it.

#   ma?n	mn	    1 match
#           man	    1 match
#           maaan	No match (more than one a character)
#           main	No match (a is not followed by n)
#           woman	1 match


# {} - Braces Consider this code: {n,m}. This means at least n, 
# and at most m repetitions of the pattern left to it.

#   a{2,3}	abc dat	    No match
#           abc daat	1 match (at daat)
#           aabc daaat	2 matches (at aabc and daaat)
#           aabc daaaat	2 matches (at aabc and daaaat)

#   [0-9]{2,4}      ab123csde	    1 match (match at ab123csde)
#                   12 and 345673	3 matches (12, 3456, 73)
#                   1 and 2	        No match


# | - Alternation Vertical bar | is used for alternation (or operator).

#   a|b	    cde 	No match
#           ade	    1 match (match at ade)
#           acdbea	3 matches (at acdbea)


# () - Group Parentheses () is used to group sub-patterns. 
# For example, (a|b|c)xz match any string that matches either a or b or c followed by xz

#   (a|b|c)xz	ab xz	    No match
#               abxz	    1 match (match at abxz)
#               axz cabxz	2 matches (at axzbc cabxz)


# \ - Backslash Backlash \ is used to escape various characters including all metacharacters. For example,
# \$a match if a string contains $ followed by a. Here, $ is not interpreted by a RegEx engine in a special way.
# If you are unsure if a character has special meaning or not, you can put \ in front of it. 
# This makes sure the character is not treated in a special way.

#   \Athe	the sun	    Match
#           In the sun	No match


# \A - Matches if the specified characters are at the start of a string.
# \b - Matches if the specified characters are at the beginning or end of a word.
# \B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.
# \d - Matches any digit. Equivalent to [0-9]
# \D - Matches any non-digit. Equivalent to [^0-9]
# \s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].
# \S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v].
# \w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. 
    # By the way, underscore _ is also considered an alphanumeric character.
# \W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
# \Z - Matches if the specified characters are at the end of a string.

#[1] using * asterisk
print('-----------------[1]------------------')
import re

# 'a' must appear 0 or more times between m and n
pattern = 'ma*n'

test_string = ['mn', 'man', 'maan', 'woman', 'main']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')

#[2] using + plus
print('-----------------[2]------------------')

# 'a' must appear 1 or more times between m and n
pattern = 'ma+n'

test_string = ['mn', 'man', 'maan', 'woman', 'main']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match! {result}')
    else:
        print(f'{str} - not match')

#[3] [] sqaure brackets
print('-----------------[3]------------------')
#if a string contains any character in the pattern , it will match
pattern = '[abc]' # or [^a-z] to not match any char from a-z

test_string = ['abc', 'a', 'ac', 'b', 'bbb','ccc' , 'crab', 'mm', '123']
print(f'pattern = {pattern}')
for str in test_string:  
    result = re.search(pattern, str) 
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')

#[4] . matches any character except \n
print('-----------------[4]------------------')
pattern = '.'

test_string = ['mn', 'man', 'maan', 'woman', 'main', '\n']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')
#[5] ^ match if string STARTS with specified char
print('-----------------[5]------------------')
pattern = '^m'

test_string = ['mn', 'man', 'maan', 'woman', 'main']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')
#[6] $ check if string ended with a pattern
print('-----------------[6]------------------')
pattern = 'a$'

test_string = ['amna', 'man', 'maan', 'woman', 'maim']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')

#[7] ? zero or ONE occurence, like * and + 
print('-----------------[7]------------------')
pattern = 'ma?n'

test_string = ['mn', 'man', 'maan', 'woman', 'main']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')
#[8] {}
print('-----------------[8]------------------')
pattern = "a{2,4}"

test_string = ['mn', 'man', 'maan', 'woman', 'maaan', 'maaaaaan']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')

#[9] | alternation symbol Or symbol
print('-----------------[9]------------------')
pattern = "i|a"

test_string = ['mn', 'man', 'maan', 'woman', 'mni']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')

#[10] () parenthesis
print('-----------------[10]------------------')
#search for a followed by an i
pattern = "(a)i"

test_string = ['mn', 'man', 'maan', 'woman', 'main']

print(f'pattern = {pattern}')
for str in test_string:
    result = re.search(pattern, str)
    if result:
        print(f'{str} - match!')
    else:
        print(f'{str} - not match')

# re.match match string if it is in the beginning
# re.search match the first occurence

#[11] re.findall return a list of the matches
print('-----------------[11]------------------')

import re

pattern = r'\d+'  # Match one or more digits
text = "I have 123 apples and 456 oranges."

matches = re.findall(pattern, text)

print(matches)

#[12] re.sub returns a new string where you replace the matched with a specified string
print('-----------------[12]------------------')
# Program to remove all whitespaces

string = 'abc 12\
de 23 \n f45 6'

pattern = '\s+'

replacement_string = ''
new_string = re.sub(pattern, replacement_string, string) 
print(new_string)

# Output: abc12de23f456

#[13] re.finditer()
print('-----------------[12]------------------')
text = 'my phone got lost damn phone'
for match in re.finditer('phone', text):
    print(match.span()) # use .group() to print the string











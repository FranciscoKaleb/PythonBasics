


line_count = 0
string_holder = ''

f = open('[10]Files/wikiText1000Lines.txt', 'w' , encoding = 'utf-8')
with open("[10]Files/TextFiles/wiki.xml", 'r', encoding = 'utf-8') as fileobject:
    for line in fileobject:
        print(line)
        line_count = line_count + 1
        if line_count%1000000 == 0:
            print(line_count)
        f.write(f"{line}")
        if line_count == 10000:
            break
f.close()

print(line_count) 
# 1374672093  or 1.4 billion lines






















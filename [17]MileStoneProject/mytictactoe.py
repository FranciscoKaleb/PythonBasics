





a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '

marked_list = []

def xchange_board(m):
    global a1,a2,a3,c1,c2,c3,b1,b2,b3,board,xturn,oturn,marked_list
    valid_input = True
    for mem in marked_list:
        if m == mem:
            print('position taken, try again')
            valid_input = False
            break
        else:
            valid_input = True
    if game_end == False and valid_input == True:
        if m == 'a1':
            a1 = 'x'
            xturn = False
            marked_list.append(m)
        if m == 'a2':
            a2 = 'x'
            xturn = False
            marked_list.append(m)
        if m == 'a3':
            a3 = 'x'
            xturn = False
            marked_list.append(m)
        if m == 'b1':
            b1 = 'x'
            xturn = False
            marked_list.append(m)
        if m == 'b2':
            b2 = 'x'
            xturn = False
            marked_list.append(m)
        if m == 'b3':
            b3 = 'x'
            xturn = False
            marked_list.append(m)
        if m == 'c1':
            c1 = 'x'
            xturn = False
            marked_list.append(m)
        if m == 'c2':
            c2 = 'x'
            xturn = False
            marked_list.append(m)
        if m == 'c3':
            c3 = 'x'
            xturn = False
            marked_list.append(m)
        if xturn == False:
            oturn = True
        else:
            print('there is no such field, try again')
        
        board = f'a |{a1}|{a2}|{a3}|\n'\
            f'b |{b1}|{b2}|{b3}|\n'\
            f'c |{c1}|{c2}|{c3}|\n'\
            '   1 2 3'
        check_winner()
def ochange_board(m):
    global a1,a2,a3,c1,c2,c3,b1,b2,b3,board,oturn,xturn,marked_list
    valid_input = True
    for mem in marked_list:
        if m == mem:
            print('position taken, try again')
            valid_input = False
            break
        else:
            valid_input = True
    if game_end == False and valid_input == True:
        if m == 'a1':
            a1 = 'o'
            oturn = False
            marked_list.append(m)
        if m == 'a2':
            a2 = 'o'
            oturn = False
            marked_list.append(m)
        if m == 'a3':
            a3 = 'o'
            oturn = False
            marked_list.append(m)
        if m == 'b1':
            b1 = 'o'
            oturn = False
            marked_list.append(m)
        if m == 'b2':
            b2 = 'o'
            oturn = False
            marked_list.append(m)
        if m == 'b3':
            b3 = 'o'
            oturn = False
            marked_list.append(m)
        if m == 'c1':
            c1 = 'o'
            oturn = False
            marked_list.append(m)
        if m == 'c2':
            c2 = 'o'
            oturn = False
            marked_list.append(m)
        if m == 'c3':
            c3 = 'o'
            oturn = False
            marked_list.append(m)
        if oturn == False:
            xturn = True
        else:
            print('there is no such field, try again')
        board = f'a |{a1}|{a2}|{a3}|\n'\
            f'b |{b1}|{b2}|{b3}|\n'\
            f'c |{c1}|{c2}|{c3}|\n'\
            '   1 2 3'
        check_winner()

def check_winner():
    global game_end
    if a1 == a2 == a3 == 'x' or a1 == b1 == c1 == 'x' or a3 == b3 == c3 == 'x' or c1 == c2 == c3 == 'x' or a2 == b2 == c2 == 'x' or b1 == b2 == b3 == 'x' or a1 == b2 == c3 == 'x' or a3 == b2 == c1 == 'x':
        print('X winsss!!!!!!!!!!!!')
        game_end = True
    if a1 == a2 == a3 == 'o' or a1 == b1 == c1 == 'o' or a3 == b3 == c3 == 'o' or c1 == c2 == c3 == 'o' or a2 == b2 == c2 == 'o' or b1 == b2 == b3 == 'o' or a1 == b2 == c3 == 'o' or a3 == b2 == c1 == 'o':
        print('O winsss!!!!!!!!!!!!')
        game_end = True

board = f'a |{a1}|{a2}|{a3}|\n'\
        f'b |{b1}|{b2}|{b3}|\n'\
        f'c |{c1}|{c2}|{c3}|\n'\
         '   1 2 3'
      
print(board)


game_end = False
xturn = True
oturn = False

def check_list():
    global game_end
    if len(marked_list) == 9:
        print('draw')
        game_end = True
        

while game_end == False:
    if game_end == False and xturn == True:
        print('X turn')
        x = input()
        xchange_board(x)
        print(board)
        check_list()
    if game_end == False and oturn == True:
        print('O turn')
        o = input()
        ochange_board(o)
        print(board)
        check_list()
    pass

# being able to tell if game has no winner
    # after marking, if program detects that all square are filled, print (draw)












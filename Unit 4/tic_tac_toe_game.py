# Full tic tac toe game
b = {'t': [' ',' ',' '],
     'm': [' ',' ',' '],
     'b': [' ',' ',' ']}

print(b['t'][0],'|',b['t'][1],'|', b['t'][2], sep='')
print('-' * 5)
print(b['m'][0],'|',b['m'][1],'|', b['m'][2], sep='')
print('-' * 5)
print(b['b'][0],'|',b['b'][1],'|', b['b'][2], sep='')

print('Welcome to tic tac toe')

locations = ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'bl', 'bm', 'br']

for i in range(9):  # There are a max of 9 turns on the board
    if i % 2 == 0:
        print('Player X: please type one of the following commands:')
        print('tl, tm, tr, ml, mm, mr, bl, bm, br which stands for top-left, top-middle, etc')
        x_turn = input().strip().lower()
        if x_turn in locations:
            locations.remove(x_turn)  #remove location from list so it can't be used again
            if x_turn == 'tl':
                b['t'][0] = 'X'
            elif x_turn == 'tm':
                b['t'][1] = 'X'
            elif x_turn == 'tr':
                b['t'][2] = 'X'
            elif x_turn == 'ml':
                b['m'][0] = 'X'
            elif x_turn == 'mm':
                b['m'][1] = 'X'
            elif x_turn == 'mr':
                b['m'][2] = 'X'
            elif x_turn == 'bl':
                b['b'][0] = 'X'
            elif x_turn == 'bm':
                b['b'][1] = 'X'
            else:
                b['b'][2] = 'X'
        else:
            print('Not a valid location. You forfeit your turn.')

    else:
        print('Player O: please type one of the following commands:')
        print('tl, tm, tr, ml, mm, mr, bl, bm, br which stands for top-left, top-middle, etc')
        o_turn = input().strip().lower()
        if o_turn in locations:
            locations.remove(o_turn)  #remove location from list so it can't be used again
            if o_turn == 'tl':
                b['t'][0] = 'O'
            elif o_turn == 'tm':
                b['t'][1] = 'O'
            elif o_turn == 'tr':
                b['t'][2] = 'O'
            elif o_turn == 'ml':
                b['m'][0] = 'O'
            elif o_turn == 'mm':
                b['m'][1] = 'O'
            elif o_turn == 'mr':
                b['m'][2] = 'O'
            elif o_turn == 'bl':
                b['b'][0] = 'O'
            elif o_turn == 'bm':
                b['b'][1] = 'O'
            else:
                b['b'][2] = 'O'
        else:
            print('Not a valid location. You forfeit your turn.')

    print(b['t'][0],'|',b['t'][1],'|', b['t'][2], sep='')
    print('-' * 5)
    print(b['m'][0],'|',b['m'][1],'|', b['m'][2], sep='')
    print('-' * 5)
    print(b['b'][0],'|',b['b'][1],'|', b['b'][2], sep='')

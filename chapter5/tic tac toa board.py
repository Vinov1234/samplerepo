theboard ={'top-l':'', 'top-m': '',  'top-r':'', 'mid-l':'','mid-m':'','mid-r':'',
           'low-l':'' ,'low-m':'', 'low-r':''}
def printbord(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m']+ '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m']+ '|' + board['low-r'])
    print('-+-+-')
    turn = 'x'
    for i in range(9):
        printbord(theboard)
        print('turn for '+ turn +' move on which space?')
        move = input()
        thebord[move] = turn
        if turn =='x':
            turn ='0'
        else:
            turn = 'x'
printbord(theboard)            
    
                

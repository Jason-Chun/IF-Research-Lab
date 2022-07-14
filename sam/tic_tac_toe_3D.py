game = True
turn = 1 
used = []
board = [[[' ']*3, [' ']*3, [' ']*3],
         [[' ']*3, [' ']*3, [' ']*3],
         [[' ']*3, [' ']*3, [' ']*3]]

def print_board(board3d):
    for board2d_cnt, board2d in enumerate(board3d):        
        prefix = ' ' if board2d_cnt>0 else '  '
        print(prefix+' '*5, '-'*9)    
        for row_cnt, row in enumerate(board2d):
            thing ='/'+' /'.join(row)+' /'
            print(prefix+' '*2*(2-row_cnt) + thing)
            print(prefix+' '*2*(2-row_cnt) + '-'*9)
            
def didThisGuyWin_check_board(board, mark):
  check_dia = 0 
  check_op_dia = 0

  for z in range(0,3):
    check_row = 0
    check_col = 0

    if board[z][z] == mark:
      check_dia += 1
      if check_dia == 3:
        return True

    if board[z][2-z] == mark:
      check_op_dia += 1
      if check_op_dia == 3:
        return True

    for v in range(0,3):
      if board[z][v] == mark:
        check_row += 1
        if check_row == 3:
          return True

      if board[v][z] == mark:
        check_col += 1
        if check_col == 3:
          return True

  return False                    
                

def didThisGuyWin(board, mark):
    
    # check boards with the same X
    for i in range(3):
        if didThisGuyWin_check_board(board[i], mark):
            return True

    # check boards with the same Y
    for i in range(3):
        board_temp = [['','',''],['','',''],['','','']]
        for j in range(3):
            for k in range(3):
                board_temp[j][k]=board[j][i][k]

        if didThisGuyWin_check_board(board_temp, mark):
            return True


    # check boards with the same Z
    for i in range(3):
        board_temp = [['','',''],['','',''],['','','']]
        for j in range(3):
            for k in range(3):
                board_temp[j][k]=board[j][k][i]

        if didThisGuyWin_check_board(board_temp, mark):
            return True

    # check boards with diagonal plane - slicing forwward
    for i in range(3):
        board_temp = [['','',''],['','',''],['','','']]
        for j in range(3):
            for k in range(3):
                board_temp[j][k]=board[j][j][k]

        if didThisGuyWin_check_board(board_temp, mark):
            return True

    # check boards with diagonal plane - slicing backward
    for i in range(3):
        board_temp = [['','',''],['','',''],['','','']]
        for j in range(3):
            for k in range(3):
                board_temp[j][k]=board[2-j][j][k]

        if didThisGuyWin_check_board(board_temp, mark):
            return True

    return False




# player1 = input("Please select a for row in boardnumber where you would like to put your mark: ")
print_board(board)
prompt = "\nPlease enter the number position you would like to put you mark in: "


while game:
  turn += 1

  play = input(prompt)

  if play in used:
    print("\nSorry there is already a piece there")
    continue
  
  used.append(play)

  pos=[int(x) for x in play.split(',')]

  if turn % 2 == 0:
    mark = "x"
  else:
    mark = "o"

  print(pos)
  board[pos[0]][pos[1]][pos[2]] = mark

  
  # print(board)
  print_board(board)

  if didThisGuyWin(board, mark):
    print(f"Yay, {mark} wins!!")
    break

#print_board(board)
# issues
#   1. wining criteria
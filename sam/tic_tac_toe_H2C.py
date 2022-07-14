
import random

game = True
turn = 1 
used = []
unused = ['1', '2', '3', '4', '5','6','7','8','9']
board = [ ['1', '2', '3' ], ['4','5','6' ], ['7','8','9' ]]
# board = [ ' ', ' ', ' ', ' ',' ',' ' , ' ',' ',' ' ]

def didThisGuyWin(board, mark):
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


def print_board(board):
  stuff = 0
  for b in board:
    thing = ' |'.join(b)
    print(thing)
    if stuff < 2:
     print('--------')
     stuff += 1

def computer(unused):
  thing = random.choice(unused)
  print("computer choose", thing)
  return thing



# player1 = input("Please select a for row in boardnumber where you would like to put your mark: ")
coordination = { "1" : [0, 0], "2" : [0, 1], "3" : [0, 2], 
                 "4" : [1, 0], "5" : [1, 1], "6" : [1, 2],
                 "7" : [2, 0], "8" : [2, 1], "9" : [2, 2] }

print_board(board)

prompt = "\nPlease enter the number position you would like to put you mark in: "


while game:
  turn += 1

  if turn % 2 == 0:
    mark = "x"
    play = input(prompt)
  else:
    mark = "o"
    play = computer(unused)
 
  if play in used:
    print("\nSorry there is already a piece there")
    continue
  
  used.append(play)  
  unused.remove(play)
  
  pos=coordination[play]

  board[pos[0]][pos[1]] = mark

  # for row in board:
  #   print(row)
  print_board(board)

  if didThisGuyWin(board, mark):
    print(f"Yay, {mark} wins!!")
    break

#print_board(board)
# issues
#   1. wining criteria


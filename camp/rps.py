import random

play = True

scenarios = {'rock' : {'rock' : "It's a Draw",
                         'paper' : 'Computer Wins!',
                         'scissor' : 'Player Wins!'},
             'paper' : {'rock' : 'Player Wins!',
                         'paper' : "It's a Draw",
                         'scissor' : 'Computer Wins!'},
             'scissor' : {'rock' : 'Computer Wins!',
                         'paper' : 'Player Wins!',
                         'scissor' : "It's a Draw"}}

def announce(comp, player):
  print(f"Computer chooses: {comp}")
  print(f"Player chooses: {player}")

while play:

  signs = ['rock', 'paper', 'scissor']

  comp = random.choice(signs)

  player = input(f"""\nChoose between: rock, paper, or scissor 
(If you would like to quite enter 'q'): """)

  player.lower()

  if player == 'q':
    break

  if player not in signs:
    print(f"'{player}' is not a valid answer.")
    continue

  print(f"\nComputer chooses: {comp}")
  print(f"Player chooses: {player}")
  print(scenarios[player][comp])

# Don't do what I did first and do all the below
  
"""if comp == player:
    announce(comp,player)
    print("It's a Draw")
    continue
    
  if comp == 'rock' and player == 'paper':
    announce(comp, player)
    print("Player wins!")
    continue
    
  if player == 'rock' and comp == 'paper':
    announce(comp, player)
    print("Computer wins!")
    continue
    
  if comp == 'rock' and player == 'scisssor':
    announce(comp, player)
    print("Computer wins!")
    continue
    
  if player == 'rock' and comp == 'scissor':
    announce(comp, player)
    print("Player wins!")
    continue

  if comp == 'scissor' and player == 'paper':
    announce(comp, player)
    print("Computer wins!")
    continue
    
  if player == 'scissor' and comp == 'paper':
    announce(comp, player)
    print("Player wins!")
    continue
  """
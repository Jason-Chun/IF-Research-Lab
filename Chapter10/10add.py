while True:
  print(f"\nenter 'q' to quit")
  try:
    ask = input("Give me a number:")
    if ask == 'q':
      break
    ask = int(ask)
    two = input("One more number:")
    if two == 'q':
      break
    two = int(two)
    ans = ask + two
    
  except ValueError:
    print("You didn't enter a number")
  
  else:
    print(ans)
#number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = range(150)

for numbers in number:
  remainder = numbers % 10
  #print(numbers, remainder)
  
  #if numbers == 11 or 12 or 13:
  if numbers % 100  in [11, 12, 13]:
    print(f"{numbers}th")
  elif remainder == 1:
    print(f"{numbers}st")
  elif remainder == 2:
    print(f"{numbers}nd")
  elif remainder == 3:
    print(f"{numbers}rd")
  else:
    print(f"{numbers}th")
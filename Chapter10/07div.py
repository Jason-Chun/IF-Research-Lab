
try:
  print(5/0)
except ZeroDivisionError:
  print('no')

print("give 2 num and i'll div")
print("enter 'q' to quit")

while True:
  first = input('first number:')
  if first == 'q':
    break
  second = input('second number:')
  if second == 'q':
    break
  try:
    ans = int(first)/ int(second)
  except ZeroDivisionError:
    print('no')
  else:
    print(ans)
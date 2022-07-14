def formated(first, last):
  full = f"{first} {last}"
  return full.title()

while True:
  print("\nPlease tell me your name: ")
  print("type 'q' anytime to quit")
  f_n = input("First name: ")
  if f_n == 'q':
     break
  l_n = input("Last name: ")
  if l_n == 'q':
      break
  forname = formated(f_n, l_n)
  print(f"\nHello, {forname}")

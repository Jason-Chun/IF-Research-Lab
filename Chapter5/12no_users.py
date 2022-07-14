users = ['Jason', 'Jaden', 'Philip', 'Admin', 'Sam']

for user in users:
  if user == 'Admin':
    print("Hello Admin would you like a statu report?")
  else:
    print(f"Hello {user}")

users = ['sam']
if users:
  for user in users:
    # if users == []:
    #   print("WE NEED MORE USERS!!!")
    if user == 'Admin':
      print("Hello Admin would you like a statu report?")
    else:
      print(f"Hello {user}")
else:
  print("We need more users")
#how make this work?
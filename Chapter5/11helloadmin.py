users = ['Jason', 'Jaden', 'Philip', 'Admin', 'Sam']

for user in users:
  if user == 'Admin':
    print("Hello Admin would you like a status report?")
  else:
    print(f"Hello {user}")
values = [ 2, 13, 50, 8, 9, 7, 12, 30, 1]
target = 9

# for v in values:
#   for f in values:    
#     if v + f == target:
#       print("yay", v, f)
#       break

for i in range(len(values)):
  for j in range(len(values)):
    if j < i:
      continue
    if values[i] + values[j] == target:
      print("yay",values[i], values[j])

print("="*50)

for i in range(len(values)):
  for j in range(i+1, len(values)):
    if values[i] + values[j] == target:
      print("yay",values[i], values[j])
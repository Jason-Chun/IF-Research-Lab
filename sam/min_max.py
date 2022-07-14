# print out maximum value / minimum value of the list

scores = [20, 10, 90, 92, 80, 23, 65, 95, 98, 79, 78, 80, 92, 95]
# print(max(scores))
# print(min(scores))
total = 0
for s in scores:
  if s > total:
    total = s
print(total)

total = 100
for s in scores:
  if s < total:
    total = s
print(total)
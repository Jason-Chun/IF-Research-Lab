# code the program that can compute an average of the given list

scores = [20, 10, 100, 92, 80, 23, 65, 100, 98, 79, 78, 80, 92, 95]

total = 0
for score in scores:
  total += score
  #print(f"{score}, {total}")
print("Average=", total/len(scores))

total = 1
for score in scores:
  total *= score
  #print(f"{score}, {total}")
print("Product=", total)
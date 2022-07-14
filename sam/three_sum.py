numbers = [3, 7, 9, 12, 4, 10, 6, 2, 1, 20, 40, 60]

for n in range(len(numbers)):
  for u in range(n +1, len(numbers)):
    if numbers[n] + numbers[u] in numbers:
      print(f"{numbers[n]} + {numbers[u]} = {numbers[n]+numbers[u]}")
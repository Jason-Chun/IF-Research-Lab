for value in range(1,5):
  print(value)
numbers = list(range(1,6))
print(numbers)
even_number = list(range(2, 11, 2))
print(even_number)
squares = []
for value in range(1, 11):
  square = value**2
  squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
  squares.append(value**2)
print(squares)

#list comprehension
square =[value**2 for value in range(1,11)]
print(square)
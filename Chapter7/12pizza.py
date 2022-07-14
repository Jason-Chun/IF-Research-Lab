prompt = "\nPlease write a pizza topping you would like"
prompt += "\nEnter 'quit' when you are done: "

while True:
  topping = input(prompt)
  if topping == 'quit':
    break
  else:
    print(f"I'll add {topping}")

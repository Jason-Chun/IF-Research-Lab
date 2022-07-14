def greet(name):
  for names in name:
    msg  = f"Hello, {names.title()}!"
    print(msg)

us = ['birb', 'borb', 'rorb']
greet(us)

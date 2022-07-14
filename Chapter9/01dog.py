class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sit(self):
    print(f"{self.name} is now sitting")

  def roll(self):
    print(f"{self.name} is now rolling over")

my_dog = Dog('will', 6)
your_dog = Dog('lucy', 4)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
my_dog.sit()
my_dog.roll()


print(f"My your dog's name is {your_dog.name}")
print(f"My your dog's age is {your_dog.age}")
your_dog.sit()
your_dog.roll()
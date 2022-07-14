class Car:
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer = 0 

  def get(self):
    big = f"{self.year} {self.make} {self.model}"
    return big.title()

  def r_odometer(self):
    print(f"This car has {self.odometer} miles on it.")

  def up(self, mileage):
    if mileage >= self.odometer:
      self.odometer = mileage
    else:
      print("You can't roll back an odometer")

  def inc(self, mile):
    self.odometer += mile
    
new = Car('audi', 'a4', '2019')
print(new.get())
new.r_odometer()

new.odometer = 23
new.r_odometer()

new.up(24)
new.r_odometer()

used = Car('subaru', 'outback', 2015)
print(used.get())

used.up(23_500)
used.r_odometer()

used.inc(100)
used.r_odometer()
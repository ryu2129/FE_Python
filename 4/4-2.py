# %%
class Car:
  kind = 'car'
  def run(self):
    print('Car is runnninng')

# %%
Car.kind
# %%
tesla = Car()
# %%
tesla.run()
# %%
class Truck(Car):
  pass
# %%
cybertruck = Truck('Cyber Truck')
print(cybertruck.name)
# %%
class Car:
  def __init__(self, name):
      self.name = name
# %%
tesla = Car('model 3')
# %%
print(tesla.name)
# %%
class Car:
  def exclaim(self):
    print('I am a car.')

class Truck(Car):
  def exclaim(self):
      print('I am a truck.')
  def baggage(self):
    print('I can carry baggage.')
# %%
tesla = Car()
cybertruck = Truck()
tesla.exclaim()
cybertruck.exclaim()
# %%
cybertruck = Truck()
cybertruck.baggage()
# %%
class Car:
  def exclaim(self):
    print('I am a car.')

class Truck(Car):
  def exclaim(self):
      super().exclaim()
      print('I am a truck.')
# %%
cybertruck = Truck()
cybertruck.exclaim()
# %%
class Dog:
  count = 0
  def __init__(self, name):
    self.name = name
    Dog.count += 1
  @classmethod
  def display(cls):
    print('Dogクラスには、犬が', cls.count,'匹います')
  def __repr__(self):
    return 'Dog object' + self.name
# %%
pochi = Dog('ポチ')
shiro = Dog('シロ')
hachi = Dog('ハチ')
print('犬の名前:', pochi.name,shiro.name,hachi.name,)
print('犬の数:', Dog.count)
Dog.display()
# %%
pochi = Dog('ポチ')
print(pochi)
# %%
from enum import Enum, auto

class Week(Enum):
  MONDAY = auto()
  TUESDAY = auto()
  WEDNESDAY = auto()
  THURSDAY = auto()
  FRISDAY = auto()
  SATURAY = auto()
  SUNDAY = auto()
# %%
week_today = Week.SUNDAY
print(week_today)
# %%
print(Week.SUNDAY.name, Week.SUNDAY.value)
# %%
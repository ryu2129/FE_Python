# %%
class Dog:
  def cry(self):
    print('わんん！')
# %%
pochi = Dog()
shiro = Dog()
# %%
pochi.cry()
# %%
class Shibainu(Dog):
  def wait(self):
    print('matei!')
# %%
hachi = Shibainu()
hachi.wait()
# %%
hachi.cry()
# %%
from abc import ABCMeta, abstractclassmethod

class Animal(metaclass = ABCMeta):
  @abstractclassmethod
  def cry(self):
    pass

class Dog(Animal):
  def cry(self):
    print('わん')

class Cat(Animal):
  def cry(self):
    print('にゃー')

# %%
pochi = Dog()
tama = Cat()

pochi.cry()
tama.cry()
# %%
class Dog:
  def __init__(self,name,weight):
    self.name = name
    self.__weight = weight
# %%
pochi = Dog('ぽち', 20)
print(pochi.name)
# %%

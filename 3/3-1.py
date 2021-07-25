# %%
def triangle_area(base, height):
  area = base * height / 2
  return area

# %%
area = triangle_area(5, 3)
print(area)
# %%
def sum_list(digitlist):
  sum_digit = 0
  for digit in digitlist:
    if digit.isdigit():
      sum_digit += int(digit)
  return sum_digit
# %%
digitlist = ['1', '4', 'abc']
sum_digit = sum_list(digitlist)
print(sum_digit)

# %%
def triangle_area(base, height=1):
  area = base * height / 2
  return area

# %%
area = triangle_area(5)
print(area)
# %%
pow(10, -2)
# %%
drinklist = ['coffee', 'tea', 'water']
print(list(enumerate(drinklist)))
# %%
for i, drink in enumerate(drinklist):
  print(i, drink)
# %%
numlist = [1, 2, 4]
def double(x):
  return x * 2
list(map(double, numlist))
# %%
numlist = [1, 3, 6, 8]
def even_three_div(x):
  return x % 3 == 0
list(filter(even_three_div, numlist))

# %%
meallist = ['steak', 'salad', 'dessert']
drinklist = ['coffee', 'tea', 'water']
list(zip(meallist, drinklist))
# %%
dict_a = dict(steak=1, salad=2, dessert=3)
dict_a
# %%
meallist = ['steak', 'salad', 'dessert']
numlist = [1, 2, 3]
dict_a = dict(zip(meallist, numlist))
dict_a
# %%
double = lambda x : x * 2
double(2)
# %%
month_name = [(1, 'January'),(2, 'February'),(3, 'March')]
month_name.sort(key = lambda x : x[1])
month_name
# %%
def variable_args(first, *args):
  print(args)

variable_args(1, 2, 3)
# %%
def double(x):
  x = x * 2
  return x
x = 1
y = double(x)
print(x, y)
# %%
def list_mod(original):
  original[1] = 'Apple'

vegetables = ['Carrot', 'Potato', 'Pampkin']
list_mod(vegetables)
vegetables
# %%
lista = [1,2,3]
listb = lista
listb[1] = 4
print(lista, listb)
# %%
import copy
lista = [1, 2, 3]
listb = copy.copy(lista)
listb[1] = 4
print(lista, listb)
# %%
lista = [[1,2,3], [4,5,6]]
listb = copy.deepcopy(lista)
listb[1][1] = 7
print(lista, listb)
# %%
def count_up():
  n = 1
  while True:
    yield n
    n += 1
# %%
generator = count_up()
for num in generator:
  print(num, end=' ')
  if num == 7:
    break
# %%
for num in generator:
  print(num, end=' ')
  if num == 15:
    break
# %%
def wrapping(contents):
  print('---- start ----')
  contents
  print('----  end  ----')
# %%
@wrapping
def contents():
  print('This is detail')
# %%
def contents():
  print('This is detail')
contents = wrapping(contents)
# %%

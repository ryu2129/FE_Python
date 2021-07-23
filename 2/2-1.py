#!/usr/bin/env python
# coding: utf-8

# In[1]:

fp = open('sample.txt', 'wt')
fp.write('This is sample1.¥n')
fp.write('This is sample2.¥n')
fp.close()

# %%
fp = open('sample.txt', 'rt')
for line in fp:
  print(line, end='')
# %%
with open('sample.txt', 'rt') as fp:
  data = fp.read()

for line in data:
  print(line, end='')

# %%
print('left', 'right', sep='|')

# %%
for i in range(5):
  print(i, end=' ')
# %%
with open('sample.txt', 'at') as fp:
  print('Hello, World!', file=fp)
# %%
name = 'jun'
age = 36
f'My name is {name}.{age} old.'
# %%
string = 'My name is {}.{} old.'
string.format(name, age)

# %%
'My name is '+name+''+str(age)+'old.'
# %%
'{0} and {1}'.format('fish', 'chip')
# %%
'{1} and {0}'.format('fish', 'chip')
# %%
'My name is {name}.{age} old.'.format(name='ルッツ', age=18)
# %%

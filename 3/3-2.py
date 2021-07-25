# %%
def search(data, target):
  for i in range(len(data)):
    if data[i] == target:
      return i
    return -1
# %%
data = [1,2,3,4,5,6,7,8,9]
target = 7
print("要素番号{}にデータ{}を見つけました。".format(search(data, target),target))
# %%
def search(data, target):
  start, end = 0, len(data)
  while start <= end:
    i = (start + end) // 2
    if data[i] == target:
      return i
    elif data[i] < target:
      start = i + 1
    else:
      end = i - 1
  return -1
# %%
def f(n):
  if n <= 1:
    return 1
  else:
    return n + f(n-1)
# %%
print(f(5))
# %%
A, B, C = [1,2,3]
# %%
def f():
  if not A:
    pass
  else:
    C.append(A.pop())
    f()
    B.append(C.pop())
# %%
f(A,B, C)
# %%

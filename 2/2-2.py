
# %%
from os import EX_CANTCREAT


20/0
# %%
'No.'+1
# %%
int('Hello')
# %%
try:
  d = int(input('数字を入れてください>'))
  print( d * 2 )
except ValueError:
  print('それは数字じゃないぞ!')
# %%
try:
  fp = open('sample.txt', 'rt')
  line = fp.readline()
  num = int(line)
except OSError:
  print('OSのエラーです')
except (ValueError, ZeroDivisionError, TypeError):
  print('数値演算のエラーです')
except Exception:
  print('一般的なエラーです')
else:
  print('結果は{}です。', num)
finally:
  fp.close()
# %%
class AnonymousError(Exception):
  pass

try:
  raise AnonymousError
except AnonymousError:
  print('AnonyMouseErrorが発生したよ')
# %%

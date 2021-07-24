# %%
import datetime
print(datetime.date.today())
# %%
from datetime import date
print(date.today())
# %%
import numpy as np
a = np.array([[1, 2],[3,4]])
print(a)
# %%
import datetime
dir(datetime)
# %%
import requests
url = "https://www.wakuwakustudyworld.co.jp"
response = requests.get(url)
print(response.status_code)
# %%

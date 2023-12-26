# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# data.head()

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)
print('______________________')

data = pd.DataFrame({'whoAmI': lst})
print(data.head(n=20))
print('______________________')

data.loc[data['whoAmI'] == 'robot', 'col_1'] = 1
data.loc[data['whoAmI'] != 'robot', 'col_1'] = 0
data.loc[data['whoAmI'] == 'human', 'col_2'] = 1
data.loc[data['whoAmI'] != 'human', 'col_2'] = 0

print(data.head(n=20))
# print('______________________')
# print(data.info())


#! importing libraries
#* keyword library as alias
#* example: import pandas as pd

import pandas as pd
# df = pd.DataFrame()
# df['numbers'] = [1, 2, 3]
# df['strings'] = ['a', 'b', 'c']
# df # this can be printed in terminal
# print(df)



import matplotlib.pyplot as plt
# plt.bar(['a', 'b', 'c'], [5, 2, 4])
# plt.plot([2,40,80],[10,2,7])

plt.show()


#! IMPORTING WITHOUT AN ALIAS
# import math
# m = math.sqrt(144) #* output: 12
# print(m)

# import random
# r = random.randint(10, 20) #* output: 13
# print(r)



#! READ_CSV
#* variable = pandas.method(file path)
df = pd.read_csv('./chapter 1/weather_data.csv') 
df2 = pd.read_csv('./chapter 1/scores_data.csv') 
print(df)
print()
print(df2)

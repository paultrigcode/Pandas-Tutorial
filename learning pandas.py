# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
#To manually store data in a table, create a DataFrame.
df = pd.DataFrame(
     {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
           ],
            "Age": [22, 35,99],
            "Sex": ["male", "male", "female"],
        }
    )
# When using a Python dictionary of lists, the dictionary keys will be used as column headers and the values in each list as columns of the DataFrame.

# print(df)
# print(df['Age'])
# print(df['Name'][1])


#You can create a Series from scratch as well:
ages = pd.Series([22, 35, 58], name="Age")
# print(ages)
# print(ages[0])

#Do something with a DataFrame or Series
# print(df["Age"].min())
# print(df["Age"].max())
# print(df.describe()) #The describe() method provides a quick overview of the numerical data in a DataFrame. As the Name and Sex columns are textual data, these are by default not taken into account by the describe() method.

#Differences between a Dataframe and a Series
'''
A Series is a one-dimensional object that can hold any
 data type such as integers, 
floats and strings. Let’s take a list of items 
as an input argument and create a Series object for tha
'''
x = pd.Series([6,3,4,6])
# print(x)
# print(x[0])
y = pd.Series([6,3,4,6], index=['a', 'b', 'c', 'd'])
# print(y['a'])

data = {'abc': 1, 'def': 2, 'xyz': 3}# you can turn a python dictionary into a series
v = pd.Series(data)
# print(v)
'''
Another interesting feature in Series is 
having data as a scalar value. In that case, 
the data value gets repeated for each of the indexes defined.
'''
e = pd.Series(3, index=['a', 'b', 'c', 'd'])
# print(e)

'''
A DataFrame is a two dimensional object that can have 
columns with potential different types. 
Different kind of inputs include dictionaries, 
lists, series, and even another DataFrame.
'''

dates = pd.date_range('20170505', periods = 8)
print(dates)

df = pd.DataFrame(np.random.randn(8,3), index=dates, columns=list('ABC'))
print(df)












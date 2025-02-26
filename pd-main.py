import pandas as pd

data = {
    'name':['Alice','Bob','Charlie'],
    'Age':[25 , 30 , 35],
    'City':['New York','Los Angeles','Chicago']
}

df = pd.DataFrame(data)


print(df)
print("==================")

data1 = [
    ['Alice',25 , 'New York'],
    ['Bob' , 30 , 'Los Angeles'],
    ['Charlies',35,'Chicago']
]

df2 = pd.DataFrame(data1, columns = ['Name','Age','City'])
print(df2)
print('==================')

df3 = pd.read_csv("banklist.csv")
# print(df3.head()) # first 5 rows
# print(df3.head(10)) # first 10 rows
# print(df3.tail()) # last 5 rows

# df3.info()
df3.describe()
# df3.shape

df2['Name']
print(df2['Name'])

print(df2[['Name','Age']])
df2.iloc[1]
print(df2.iloc[1:3])

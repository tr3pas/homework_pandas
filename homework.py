import pandas as pd

data = {
    'Name': ['Alex', 'Bella', 'Chris'],
    'Age': [30, 25, 35],
    'City': ['Kyiv', 'Lviv', 'Odesa']
}
df = pd.DataFrame(data)


df['Salary'] = [50000,60000,55000]
print(df)

del df['Age']
print(df)

data1 = {'Name': ['Diana'], 'City': ['Dnipro'], 'Salary': [58000]}
df1 = pd.DataFrame(data1)

df = pd.concat([df,df1],ignore_index=True)
print(df)

df = df.drop(0,axis=0)
print(df)

df['Departament'] = 'Sales'
print(df)

df = df.drop('Salary', axis=1)
print(df)
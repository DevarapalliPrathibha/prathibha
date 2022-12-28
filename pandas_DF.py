import pandas as pd

df = pd.read_csv("C:/Users/user718/PycharmProjects/pythonProject/pokemon/pokemon_data (1).csv")
# de = pd.read
# swapping two columns
print(df)
print("################################################")
column=list(df)
column[2],column[3] = column[3],column[2]
df.columns=column
print(df)
print("################################################")
#df['Type 1'],df['Type 2']=df['Type 2'],df['Type 1']
#print(df.to_string())

#print value start with A
new1_df = df.loc[df['Name'].str.startswith('A')]
print(new1_df)
print("################################################")
#indexing values into dates
dates = pd.date_range("20010407",periods = 800)
print(dates)
print("################################################")
df['#']=dates
print(df)
print("################################################")
# sum of odd index
df['oddsum']=df.iloc[1::2,[5,6,9]].sum(axis=1)
print(df)
print("################################################")
#groupby __> sum
df1 = df.groupby('Type 1').sum()
print(df1)



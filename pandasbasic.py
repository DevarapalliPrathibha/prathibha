#dataframe = dataframe data in rows and columns(eg:tabular dataframes)
#series = list data
#dict = {'pinky':90, 'hello': 80} #panel data
import pandas as pd
import numpy as np
a = [1,2,3,4,5,6,7,'b']
series = pd.Series(a)
print(series)
print("############################################")
#to check the version of the pandas we can use _version_
#print(pd._version_)
#read-csv(comma seperated files) <60 lines) , read-json >60 lines
#csv
df = pd.read_csv('file_1.txt')
print(df)
print("############################################")
#to_string is used to print the entire data
#head() function is used to get the topdata of the document
#if we give head() then the 1st five data elements will print automatically
#tail() is opposite to head()
#non null value indicates there is no value presents, not a 0
print(df.head(2))
print("############################################")
print(df.tail(2))
print("############################################")
print(df.info()) ##info() gives more information about the dataset
print(df.index)
print("############################################")
print(df.columns)
print("############################################")
print(df.to_numpy)
print("############################################")
hi = pd.Series([1,2,3,4,np.nan])
print(hi)
print(hi[0])
print("############################################")
hello = pd.Series([1,2,3,4,5])
print(hello)
print("############################################")
date = pd.date_range("20010407",periods =6)
print(date)
print("############################################")
print(df.T)
print("############################################")
df = pd.DataFrame(np.random.randn(6,4),index=date,columns=list("ABCD"))
print(df)
print("\n")
print(df.T)
df1 = pd.DataFrame(
    {
       "a" : 2.0,
       "b" : pd.Timestamp("20010704"),
       "c" : pd.Series(1, index=list(range(4)),dtype="float32"),
       "d" : np.array([3] * 4,dtype ="int32"),
       "e" : pd.Categorical(["test","train","test","train"]),
       "f" : "hmm"
    }
)
print(df1)
print(df1.dtypes)
print(df1.T)# T = transpose(rows into columns)
#print(df1.tail(2))
#print(df.head(2))
print("\n")
#print(df["a"]>0)
#print(df[df>0])
#print(df.mean())
# STRING OPERATIONS
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print( s.str.lower())
print("\n")
# concat
df_r = pd.DataFrame(np.random.randn(10, 4))
print(df_r)
print("\n")
print(df_r[:3], df_r[3:7])
print(df_r[7:])
print("\n")
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
# join -- works just like sql join
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left)
print("\n")
print(right)
print("\n")
pd.merge(left, right, on="key")
# Grouping
# Splitting the data into groups based on some criteria
# Applying a function to each group independently
# Combining the results into a data structure
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
"D": np.random.randn(8),
    }
)
print(df)
print("\n")
df.groupby("A")[["C", "D"]].sum()
print(df.groupby(["A", "B"]).sum())
tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
df2
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
print(df)
print("\n")
# another complex data
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))
print("\n")
# time series
rng = pd.date_range("1/1/2012", periods=100, freq="S")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
print("\n")
ts.resample("5Min").sum()
import matplotlib.pyplot as plt
plt.close("all")
ts = pd.Series(np.random.randn(1000), index=pd.date_range("04/07/2001", periods=1000))
ts = ts.cumsum()
print(ts)
print("\n")
ts.plot();
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)
df = df.cumsum()
print(df)
print("\n")
plt.figure();
df.plot();
plt.legend(loc='best');












import pandas as pd
marks=pd.Series([50,20,30,60,70,55])
print(marks)

data={
    "sn":[1,2,3,4,],
    "name":["bandhan","div","aksh","abhi"],
    "city":["unnao","kanpur","basti","lucknow"],
    "age":[18,20,60,40,]
}
#df=pd.DataFrame(data)
#df.to_csv("rr.csv")
x=pd.read_csv("Pandaa.csv")
print(x)
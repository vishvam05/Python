import pandas as pd
data={
  "calories":[430,334,231],
  "duration":[50,23,13]
}
df=pd.DataFrame(data,index=["day1","day2","day3"])
print(df)
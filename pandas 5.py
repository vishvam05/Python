import pandas as pd
data={'name':['smith','parker'],'id':[102,102],"language":["python","javascript"]}
df=pd.DataFrame(data)
df.to_csv('output.csv',index=False)
print(df)
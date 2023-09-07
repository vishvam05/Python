import pandas as pd
data={'name':['smith','parker'],'id':[102,102],"language":["python","javascript"]}
data_pd=pd.DataFrame(data)
print(data_pd)
data_pd.rename(columns={'name':'Name'},inplace=True)
print("\nafter modifying :",data_pd.columns)
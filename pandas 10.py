import pandas as pd
data={'name':['smith','parker'],'id':[102,103],"language":["python","javascript"]}
info=pd.DataFrame(data)
print(info)
csv_data=info.to_csv()
print(csv_data)
csv_data=info.to_csv(na_rep="None")
print(csv_data)
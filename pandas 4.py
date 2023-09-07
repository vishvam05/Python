import pandas as pd
data={'name':['smith','parker'],'id':[102,102],"language":["python","javascript"]}
info=pd.DataFrame(data)
print("dataframe values:\n",info)
csv_data=info.to_csv()
print('\ncsv srting values',csv_data)
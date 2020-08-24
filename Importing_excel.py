#import excel sheet
#find that column which contains the address
#find distinct values

import pandas as pd 
cols=[5,6,7]
df = pd.read_excel (r'C:\Users\Pranjal\Desktop\557629_1437601_bundle_archive\IndividualDetails.xlsx', usecols=cols)

df1 = df["detected_city"] + (",") + df["detected_district"] + (",")+ df["detected_state"]
df1 =df1.unique()
print(df1)
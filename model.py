import pandas as pd
df=pd.read_csv("KRS.csv")
df['FLOW_DATE']=pd.to_datetime(df.FLOW_DATE)
df["YEAR"]=df['FLOW_DATE'].dt.year
df["MONTH"]=df['FLOW_DATE'].dt.month
df["DATE"]=df['FLOW_DATE'].dt.day
def is_int(x):
    try:
        int(x)
    except:
        return False
    return True
def is_float(x):
    try:
        float(x)
    except:
        return False
    return True

df=df[df['INFLOW_CUSECS'].apply(is_float)]
df=df[df['RES_LEVEL_FT'].apply(is_float)]

df1=df[["DATE","MONTH","YEAR","RES_LEVEL_FT","INFLOW_CUSECS","OUTFLOW_CUECS","PRESENT_STORAGE_TMC"]]

convert_c={
    'INFLOW_CUSECS':float,
    'RES_LEVEL_FT':float
}
df1=df1.astype(convert_c)

import matplotlib.pyplot as plt
plt.scatter(df1.INFLOW_CUSECS,df1.OUTFLOW_CUECS)

df1=df1[~(df1.OUTFLOW_CUECS>50000)]
df1=df1[~(df1.OUTFLOW_CUECS>50000)]

x=df1.iloc[:,:-1]
y=df1.loc[:,['PRESENT_STORAGE_TMC']]

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
model=LinearRegression()
model.fit(x_train,y_train)

a=[[16,3,2021,119.83,3416.0,3043]]
pred=model.predict(a)
print(pred)

import pickle
pickle.dump(model,open('krs.pkl','wb'))


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('finance_liquor_sales.csv')
cn=df.groupby(['zip_code','item_description'])
print(cn.agg({'bottles_sold':'sum'}))
df['sale_dollars_percentage']=df['sale_dollars']/df['sale_dollars'].sum()*100
cn=df.groupby('store_name')
print(cn.agg({'sale_dollars':'sum','sale_dollars_percentage':'sum'}))
plt.scatter(df['zip_code'],df['bottles_sold'])
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold')
plt.show()
plt.bar(df['store_name'],df['sale_dollars_percentage'])
plt.xlabel('Store Name')
plt.xticks(rotation=90)
plt.ylabel('Sale Dollars Percentage')
plt.title('Sales Percentage Per Store')
plt.show()

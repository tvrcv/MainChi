

import pandas as pd
import matplotlib.pyplot as plt

 
df = pd.read_csv('amazonDS.csv')
df = df.fillna(0)

df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)

df['Order Date'] = pd.to_datetime(df['Order Date'])

daily_orders = df.groupby('Order Date').sum()["Total Charged"]
daily_orders.plot.bar(figsize=(15,10))
plt.tight_layout()
plt.show()






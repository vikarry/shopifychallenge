import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pandas.plotting import scatter_matrix

pd.options.mode.chained_assignment = None
data = pd.read_csv("data.csv")
print(data)
print(data['order_amount'].describe())
data.plot(kind='scatter', x='shop_id', y='order_amount', title="Order amount per shop", )
# plt.show()

shop_42 = data[data['shop_id'] == 42]
shop_42['date'] = shop_42['created_at'].str.partition(' ')[0]
shop_42['date'] = pd.to_datetime(shop_42['date'], format='%Y-%m-%d')

plot_amount_42 = shop_42.plot(kind='scatter', x='date', y='order_amount', title='Shop 42 amount per order')
for i, t in enumerate(plot_amount_42.get_xticklabels()):
    if (i % 2) != 0:
        t.set_visible(False)

plot_number_42 = shop_42.plot(kind='scatter', x='date', y='total_items', title='Shop 42 item per order')
for i, t in enumerate(plot_number_42.get_xticklabels()):
    if (i % 2) != 0:
        t.set_visible(False)

shop_78 = data[data['shop_id'] == 78]
shop_78['date'] = shop_78['created_at'].str.partition(' ')[0]
shop_78['date'] = pd.to_datetime(shop_78['date'], format='%Y-%m-%d')

plot_amount_78 = shop_78.plot(kind='scatter', x='date', y='order_amount', title='Shop 78 amount per order')
for i, t in enumerate(plot_amount_78.get_xticklabels()):
    if (i % 2) != 0:
        t.set_visible(False)

plot_number_78 = shop_78.plot(kind='scatter', x='date', y='total_items', title='Shop 78 item per order')
for i, t in enumerate(plot_number_78.get_xticklabels()):
    if (i % 2) != 0:
        t.set_visible(False)

# calculate total payment and the portion contributed by shop 42 & 78
total = data['order_amount'].sum()
total_42 = shop_42['order_amount'].sum()
total_78 = shop_78['order_amount'].sum()

print("Percentage of shop 42: ", total_42/total*100)
print("Percentage of shop 78: ", total_78/total*100)

plt.show()
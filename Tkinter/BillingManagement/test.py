import pandas as pd

path = '/media/d/git/Python-Playground/Tkinter/BillingManagement/Inventory_Backup_20240602_215200.csv'

df = pd.read_csv(path, header=None, names=['itemname', 'price'])

print(df)
print(df.columns)

for index, row in df.iterrows():
    print(index, row.itemname, row.price)


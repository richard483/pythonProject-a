import pandas as pd 

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

data = pd.read_json('D:\Belajar\peye\ShopeeCodeLeague\Week1-1\contacts.json')
data100 = data.loc[0:1000]
data100.to_json('D:\Belajar\peye\ShopeeCodeLeague\Week1-1\su1000.json')

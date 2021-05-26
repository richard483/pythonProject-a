import pandas as pd 
# {"Id": 98, "Email": "DxtVenmxYlNSRxG@qq.com", "Phone": "", "Contacts": 0, "OrderId": ""}
data = pd.read_csv('D:\Belajar\peye\ShopeeCodeLeague\Week1-1\EheTehNaon.csv')

# out_df = pd.DataFrame(data, columns = ['ticket_id'])
# out_df['ticket_trace/contact'] = data['ticket_trace/contact']
# out_df.to_csv('D:\Belajar\peye\ShopeeCodeLeague\Week1-1\jwb_v3.csv', index=True)
dat = pd.DataFrame(data, columns = ['ticket_id'])
dat['ticket_trace/contact'] = data['ticket_trace/contact']

dat.to_csv(r'D:\Belajar\peye\ShopeeCodeLeague\Week1-1\neo2.csv', index=False)
print(dat)
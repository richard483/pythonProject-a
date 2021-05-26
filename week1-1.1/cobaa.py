import pandas as pd 
# {"Id": 98, "Email": "DxtVenmxYlNSRxG@qq.com", "Phone": "", "Contacts": 0, "OrderId": ""}
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
data = pd.read_json('D:\Belajar\peye\ShopeeCodeLeague\Week1-1\su1000.json')
#print(data['Email'])

#mencari email yg sama trs d simpen d 'dike'(dictionary email) indexnya
lst_mai = []
dike = {}

for i in range(1001):
    copy = False
    for j in range(len(lst_mai)):
        if(data['Email'][i] == lst_mai[j] and data['Email'][i]!=''):
            dike[data['Email'][i]].append(data['Id'][i])
            
            copy = True
    if(copy == False and data['Email'][i]!=''):
        lst_mai.append(data['Email'][i])
        dike[data['Email'][i]] =[data['Id'][i]]
#print(lst_mai, dike)

#mencari no telp yg sama trs d simpen d 'dikp'(dictionary phone) indexnya
lst_ho = []
dikp = {}

for i in range(1001):
    copy = False
    for j in range(len(lst_ho)):
        if(data['Phone'][i] == lst_ho[j] and data['Phone'][j]!=''):
            dikp[data['Phone'][i]].append(data['Id'][i])

            copy = True
    if(copy == False and data['Phone'][i]!=''):
        lst_ho.append(data['Phone'][i])
        dikp[data['Phone'][i]] = [data['Id'][i]]
#print(lst_ho, dikp)

#mencari OrderId yg sama trs d simpen d 'diko'(dictionary orderid) indexnya

lst_oi = []
diko = {}

for i in range(1001):
    copy = False
    for j in range(len(lst_oi)):
        if(data['OrderId'][i] == lst_oi[j] and data['OrderId'][j] != ''):
            diko[data['OrderId'][i]].append(data['Id'][i])

            copy = True
    if(copy == False and data['OrderId'][i]!=''):
        lst_oi.append(data['OrderId'][i])
        diko[data['OrderId'][i]] = [data['Id'][i]]
#print(lst_oi, diko)

dik_end = {}
for i in range(1001):
    if(data['Email'][i]!= ''):
        dik_end[i] = dike[data['Email'][i]]
        if(data['Phone'][i] != ''):
            dik_end[i] = dik_end[i] + dikp[data['Phone'][i]]
        if(data['OrderId'][i] != ''):
            dik_end[i] = dik_end[i] + diko[data['OrderId'][i]]

    elif(data['Phone'][i] != ''):
        dik_end[i] = dikp[data['Phone'][i]]
        if(data['OrderId'][i] != ''):
            dik_end[i] = dik_end[i] + diko[data['OrderId'][i]]
    
    elif(data['OrderId'][i] != ''):
        dik_end[i] = diko[data['OrderId'][i]]


total = []
for key in dik_end:
    a = ''
    b = 0
    dik_end[key] = list(set(dik_end[key]))
    dik_end[key].sort()
    for i in range(len(dik_end[key])-1):
        b = b + data['Contacts'][int(dik_end[key][i])]
        a = a + str(dik_end[key][i]) + '-'
    b = b + data['Contacts'][dik_end[key][len(dik_end[key])-1]]
    a = a + str(dik_end[key][len(dik_end[key])-1])
    total.append(f"{a}, {b}")

out_df = pd.DataFrame(data, columns = ['Id'])
out_df = out_df.rename(columns={'Id':'ticket_id'})
out_df['tiket_trace/contact'] = total
out_df.to_csv('D:\Belajar\peye\ShopeeCodeLeague\Week1-1\ganbare.csv', index=False)
    

print('ok')







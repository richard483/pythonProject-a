def baineri_serch(lst, awal, akhir, x):
    '''
    fuction ini mengambil variabel List, Index awal, Index akhir, dan nilai yang ingin dicari, kemudian mengeluarkan nilai x jika terdapat nilainya didalam lst, sedangkan akan mereturn -1 jika tidak ada
    '''
    mid = (awal+akhir)//2
    if(akhir>=awal):
        if(lst[mid] == x):
            return x
        elif(lst[mid]>x):
            return (baineri_serch(lst, awal, mid-1, x))
        elif(lst[mid]<x):
            return (baineri_serch(lst, mid+1, akhir, x))

    else:
        return -1



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
    lst_mai.sort()
    copy = False
    if(len(lst_mai) != 0):
        if(data['Email'][i] != '' and  baineri_serch(lst_mai, 0, (len(lst_mai)-1), data['Email'][i]) != -1):
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
    lst_ho.sort()
    copy = False
    if(len(lst_ho) != 0):
        if(data['Phone'][i] != '' and  baineri_serch(lst_ho, 0, (len(lst_ho)-1), data['Phone'][i]) != -1):
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
    lst_oi.sort()
    if(len(lst_oi) != 0):
        if(data['OrderId'][i] != '' and  baineri_serch(lst_oi, 0, (len(lst_oi)-1), data['OrderId'][i]) != -1):
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
out_df.to_csv('D:\Belajar\peye\ShopeeCodeLeague\Week1-1\ganbare_v2.csv', index=False)
    

print('ok')







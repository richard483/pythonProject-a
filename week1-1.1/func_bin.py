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

# dct = {'Saya':[1,2,3], 'Saha':[4,5,6], 'Layla':[7,8,9], 'Goat':[10,11,12], 'Bobon':[13,14,15], 'Alstromeria':[16,17,18]}
# alfa = sorted(dct)
# print(alfa)
# print(dct)
# print(baineri_serch(alfa, 0, (len(alfa)-1), 'Siapa'))

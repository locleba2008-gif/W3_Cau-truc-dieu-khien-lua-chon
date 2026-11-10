diem=float(input())
if diem>10 or diem<0:
    print('Khong hop le')
else:    
    if diem>=8 :
        print('Gioi')
    elif diem>=6.5:
        print('Kha')
    elif diem>=5:
        print('Trung binh')
    else:
        print('Yeu')            
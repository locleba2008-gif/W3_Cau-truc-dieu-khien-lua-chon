a,b=map(float,input().split())
if a==0 and b==0:
    print('Phuong trinh vo so nghiem')
elif a==0 and b!=0:
    print('Phuong trinh vo nghiem')    
elif a!=0:
    nghiem=-b/a
    print(round(nghiem,2))    
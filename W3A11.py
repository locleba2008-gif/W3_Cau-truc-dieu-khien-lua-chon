a,b,c=map(int,input().split())
if a<=0 or b<=0 or c<=0:
    print('3 so khong hop le')
else:
    if a+b>c and b+c>a and a+c>b:
        if a==b==c:
            print('Tam giac deu') 
        elif a==b!=c or a==c!=b or b==c!=a:
            print('Tam giac can')
        elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print('Tam giac vuong')
        elif  (a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2) and a==b!=c or a==c!=b or b==c!=a:
            print('Tam giac vuong can')
        else:
            print('Tam giac thuong')  
    else:
        print('Khong phai tam giac')                     
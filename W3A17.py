a,b,c,d=map(float,input().split())
q=b/a
if c==q*b and d==c*q:
    if q==int(q):
        print('Yes')
else:
    print('No')        


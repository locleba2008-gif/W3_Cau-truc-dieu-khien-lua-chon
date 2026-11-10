n=float(input())
if n==int(n):
   so_len=int(n)
   so_xuong=int(n)
   so_nguyen_gan_nhat=int(n)
elif n<0:
    so_len=int(n)
    so_xuong=int(n)-1
    if int(n)-n<0.5:
        so_nguyen_gan_nhat=int(n)
    else:
        so_nguyen_gan_nhat=int(n)-1
else:
    so_len=int(n)+1
    so_xuong=int(n)
    if n-int(n)<0.5:
        so_nguyen_gan_nhat=int(n)
    else:
        so_nguyen_gan_nhat=int(n)+1
print(so_len,so_xuong,so_nguyen_gan_nhat,sep=' ')
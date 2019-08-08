a=list(map(int,input().split(' ')))
b=a[0]
c=a[1]
d=0
while(b!=0):
  r=b%c
  d+=r
  b=b//r
print(d+b)

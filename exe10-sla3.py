n = 0 
c = 1
s = 0
v = 0
while c<500:
    n = n+1
    if n%2==0:
        s = n+v
        v = s
    print(s)


n = int(input('digite um número para ver sua tabuada:'))
x = 0
c = 0
while x<10:
    x = x+1
    c = x*n
    print('{}x{}={}'.format(x,n,c))
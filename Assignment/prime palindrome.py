n=int(input('Enter a number:'))
l=str(n)
g=list()
if l==l[::-1]:
    for i in range(1,n+1):
        if n%i==0:
            g.append(i)
t=list(set(g))
if len(t)==2:
    print('Prime palandrome')
else:
    h=list()
    for j in range(n+1,100000):
        x=str(j)
        if x==x[::-1]:
            for k in range(1,j+1):
                if j%k==0:
                    h.append(k)
            u=list(set(h))
            if len(u)==2:
                print('Next prime palandrome',x)
                break
            else:
                continue
    else:
        v=list()
        for i in range(n+1,100000):
            y=str(i)
            if y==y[::-1]:
                for j in range(1,i+1):
                    if i%j==0:
                        v.append(j)
                    m=list(set(v))
                if len(m)==2:
                    print('Next prime palandrome',y)
                    break
                else:
                    continue
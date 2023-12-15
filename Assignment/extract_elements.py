l=[4,6,4,3,3,4,3,4,3,8]
k=int(input('Enter a number:'))
g=list(set(l))
h=list()
for i in range(len(g)):
    if l.count(g[i])>k:
        h.append(g[i])
print(h)
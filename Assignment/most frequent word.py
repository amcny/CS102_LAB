f=open('D:/sample.txt','r')
p=f.read()
q=p.split('/n')
l=list(q)
g=list()
for i in range(len(l)):
    t=l[i].split('')
    g.append(t)
s=list(set(g))
d=dict()
for j in range(len(s)):
    d[s[j]]=g.count(s[j])
print(d)
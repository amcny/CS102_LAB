f = open('D:/str.txt', 'r')
p = f.read()
q = p.split('\n')
l = list(q)
g = list()
freq = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        g.append(l[i][j])
for i in range(len(g)):
    count = 0
    h = list()
    for j in range(len(g[i])):
        h.append(g[i][j])
    k = list()
    for m in range(1, len(h) + 1):
        k.append(h[-m])
    for n in range(len(k)):
        if h[n] == k[n]:
            count = count + 1
    if count == len(h):
        freq = freq + 1
print(freq)

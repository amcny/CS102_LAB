f = open('D:/Binary.txt', 'r')
p = f.read()
q = p.split('\n')
l = list(q)
g = list()
h = list()
freq = 0

for i in range(len(l)):
    t = l[i].split('')
    g.append(t)

for i in range(len(g)):
    h = g[i] + h

print(h)

m = list()

for i in range(len(h)):
    y = list(h[i])
    d = 0

    for j in range(1, len(y) + 1):
        if int(y[-i]) == 1:
            d = d + 2**(j - i)

    m.append(str(d))

f1 = open('D:/Decimal.txt', 'r')
z = f1.read()
b = z.split('\n')
c = list(b)
o = list()
r = list()

for i in range(len(c)):
    e = c[i].split('')
    o.append(e)

for i in range(len(o)):
    r = o[i] + r

print(r)

for i in range(len(m)):
    if m[i] == r[i]:
        freq = freq + 1

print(freq)

f = open('D:/students.txt', 'r')
p = f.read()
q = p.split('\n')
l = list(q)
g = list()
h = list()

for i in range(len(l)):
    t = l[i].split('')
    g.append(t)

for i in range(len(g)):
    h = g[i] + h

print(h)

m = list()

for i in range(len(h)):
    if h[i].isalpha() == True:
        m.append(h[i])

v = ['a', 'e', 'i', 'o', 'u']

for i in range(len(m)):
    for j in range(len(m[i])):
        f = str()
        if m[i][j] in v:
            for k in range(j, 0, -1):
                f = f + m[i][j]
            print(f)
n = input('Enter your password:')
l = list()
g = list()
h = list()
m = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '|', '\\', '<', '>', '?', '.', '~']

for i in range(65, 91):
    l.append(chr(i))

for j in range(97, 123):
    g.append(chr(j))

for k in range(10):
    h.append(str(k))

x = False
y = False
z = False
x1 = False

c = list(n)

if len(c) >= 8:
    print('Length of the password OK')

    for j in l:
        if c.count(j) >= 1:
            x = True
            print('Upper case in password OK')
            break
    else:
        print('UPPER CASE NOT FOUND')

    if x == True:
        for k in g:
            if c.count(k) >= 1:
                y = True
                print('Lower case OK')
                break
        else:
            print('LOWER CASE NOT FOUND')

    if y == True:
        for p in h:
            if c.count(p) >= 1:
                z = True
                print('Digits OK')
                break
        else:
            print('DIGITS NOT FOUND')

    if z == True:
        for q in m:
            if c.count(q) >= 1:
                x1 = True
                print('Special characters OK')
                break
        else:
            print('SPECIAL CHARACTERS NOT FOUND')
else:
    print('PASSWORD IS TOO SHORT')

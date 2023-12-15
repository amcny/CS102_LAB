def integer(l):
    h = list()
    for i in range(len(l)):
        if isinstance(l[i], int) and l[i] >= 0:
            h.append(l[i])
    return h

l = [1, 'a', 0, 'b', 3, 'c', -1, 2, 'd']
print(integer(l))
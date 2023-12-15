n=int(input('enter no.of elements in the list : '))
l=[]
for i in range(n):
    k=int(input('enter the element : '))
    l.append(k)
print('the list is : ',l)
e=[]
o=[]
for j in range(n):
    if(l[j]%2==0):
        e.append(l[j])
    else:
        o.append(l[j])
e.sort()
o.sort()
print('largest even number in the list : ',e[len(e)-1])
print('largest odd number in the list : ',o[len(o)-1])
n=int(input('enter no.of elements in the list : '))
l=[]
for i in range(n):
    k=int(input('enter elements in the list : '))
    l.append(k)
print('list is : ',l)
for j in range(0,n-2):
    if(l[j]==l[j+1]):
        l.remove(l[j])
print('final list : ',l)
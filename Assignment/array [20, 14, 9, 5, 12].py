l=[20, 14, 9, 5, 12]
for i in range(0,len(l)):
  for j in range(0,len(l)-1):
    if l[j]>l[j+1]:
     l[j],l[j+1]=l[j+1],l[j]
for i in range(0,len(l)):
  if l[i]==14:
   print(i)
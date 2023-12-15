f=open("sample.txt","r")
Str=f.read()
x=str.split()
vow=["A","E","I","O","U"]
spec="[@_!#$%^&*()<>?/|}{~:]"
spec=list(spec)
for i in x:
    if i[0].upper() in vow:
        print(i,"starts with vowel")
for k in x:
    if i[-1].upper() in vow:
        print(i,"Ends with vowel")
for i in x:
    if i[0].isdigit=="True":
        print(i,"starts with number")
print("The number of spaces are: ",len(x)-1)
for i in x:
    if i[0] in spec:
        print(i,"starts with special character:")
f.close()
import math
print('expansion of sin(x)')
x=int(input('enter the value of x : '))
n=int(input('enter the no.of terms : '))
s=0
for i in range(n+1):
    s+=((-1)*i)*((x*((2*i)+1))/math.factorial((2*i)+1))
print('sum : ',s)
print('Enter your DOB in DDMMYYYY')
n=int(input('Enter DOB:'))
l=str(n)
d=int(l[2]+l[3])
if len(str(n))>8:
    print('Not DOB')
else:
    if int(l[2]+l[3])>12:
        print('Not DOB')
    else:
        if (((d==1 or d==3) or (d==5 or d==7)) or (d==10 or d==12)) and int(l[4]+l[5]+l[6]+l[7])%4==0:
            print('Congratulations')
        else:
            print('Sorry')
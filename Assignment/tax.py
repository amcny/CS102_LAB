n=int(input('Enter annual income:'))
if n<=100000:
    print('No Tax')
elif n>100000 and n<=200000:
    print('Tax:',1000+(24/100)*n)
elif n>200000:
    print('tax:',2500+(30/100)*n)
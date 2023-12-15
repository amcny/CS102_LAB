def check(n):
    n=str(n)
    a=int(n[0])
    b=int(n[1])
    if a%2==0 and b%2==0:
        return True
    elif a%2 !=0 and b%2!=0:
        return True
    else:
        return False
print(check(int(input("Enter a number: "))))
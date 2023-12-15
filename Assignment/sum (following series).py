def findsum():
    ans=0
    i=1
    while i<=97:
        ans+=(i)/(i+2)
        i+=2
        return ans
    print(findsum())
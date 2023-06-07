def perfect_other(n):
    ls=list()
    for i in range(1,n//2+1):
        if n%i==0:
            ls.append(i)
    return ls
    
for i in range(1,10000):
    if i == sum(perfect_other(i)):
        print(i)
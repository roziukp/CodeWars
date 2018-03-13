#Sum of Digits / Digital Root
def digital_root(n):
    summ=0
    while n//10!=0:
        for i in str(n):
            summ+=int(i)
        n,summ=summ,0
    return n

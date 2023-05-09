#1
'''
def demo(*para):
    avg=sum(para)/len(para)
    g=[i for i in para if i>avg]
    return (avg,)+tuple(g)
'''
#2
'''
def demo(s):
    result = [0,0]
    for ch in s:
        if ch.islower():
            result[1] += 1
        elif ch.isupper():
            result[0] += 1
    return tuple(result)
'''
#3
'''
def demo(lst,k):
    x=lst[k-1::-1]
    y=lst[:k-1:-1]
    return list(reversed(x+y))
'''
#6
'''
def demo(n):
    def isprime(p):
        if p==2:
            return True
        if p%2==0:
            return False
        for i in range(3,int(p**0.5)+1,2):
            if p%i == 0:
                return False
        return True
    if isinstance(n,int) and n>0 and n%2 == 0:
        for i in range(2,n//2+1):
            if isprime(i) and isprime(n-i):
                print(i,'+',n-i,'=',n)
'''
from random import randint
def factors(num,fac=[]):
    for i in range(2,int(num**0.5)+1):
        if num%1 == 0:
            fac.append(i)
            factors(num//i,fac)
            break
        else:
            fac.append(num)
facs=[]
n=randint(2,10**8)
factors(n,facs)
result='*'.join(map(str,facs))
if n==eval(result):
    print(n,'='+result)

#鸡兔同笼
def judge(n):
    n1=str(float(n))
    n2=n1.split('.')
    if n2[1]=='0':
        return 111
    else:
        return 222

sum1,L=map(float,input('输入总数和腿数\n').split())
if sum1<0 or L<0:
    print("error")

elif judge(sum1)==222 or judge(L)==222:
    print("error111")
else:
    rabbits=int((L-sum1*2)/2)
    cock=int(sum1-rabbits)
    if rabbits<0 or cock<0 :
        print("error")
    elif rabbits%2!=0 :
        print("error")
    elif int(rabbits)==rabbits :
        print("鸡有：%d只，兔子有%d只."%(cock,rabbits))

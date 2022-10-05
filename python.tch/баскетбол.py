a1, b1=[int (i) for i in input().split()]
a2, b2=[int (i) for i in input().split()]
a3, b3=[int (i) for i in input().split()]
a4, b4=[int (i) for i in input().split()]
sum1=a1+a2+a3+a4
sum2=b1+b2+b3+b4
if sum1>sum2:
    print(1)
elif sum1<sum2:
    print(2)
else:
    print('DRAW')
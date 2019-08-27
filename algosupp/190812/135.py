A, B = map(int, input().split())
result = []
for i in range(min(A,B),max(A,B)+1):
    if i% 3 == 0 or i% 5 ==0:
        result.append(i)





Sum = sum(result)
Avg = Sum/len(result)


print('sum : {}'.format(Sum))
print('avg : {:.1f}'.format(Avg))
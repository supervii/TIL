# N = int(input())
result =[]
for i in range(1,N+1):
    if i % 5==0:
        result.append(i)
    A = sum(result)

print(A)

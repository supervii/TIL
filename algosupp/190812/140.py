arr = list(map(int, input().split()))
result = []
# while len(arr) < 20:
for i in arr:
    if i == 0: break
    result.append(i)

Sum = sum(result)
Avg = Sum//len(result)

print(Sum, Avg)





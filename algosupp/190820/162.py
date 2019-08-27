arr = list(map(int, input().split()))

for i in range(2, 10):
    arr.append((arr[i-1] + arr[i-2]) % 10)
# print(arr)

print(' '.join(map(str, arr)))

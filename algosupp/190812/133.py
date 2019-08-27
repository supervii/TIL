N = int(input())
arr = list(map(int, input().split()))

for i in arr:
    A = sum(arr)/N
print(round(A,2))
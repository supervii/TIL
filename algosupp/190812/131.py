A, B = map(int, input().split())

if A > B:
    A, B = B, A

for _ in range(min(A,B), max(A,B)+1):
    print(i, end=' ')


while A <= B:
    print(A, end=' ')
    A = A+1
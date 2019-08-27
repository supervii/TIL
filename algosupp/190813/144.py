N = int(input())
M = N * 2 - 1

for i in range(1, M + 1, 2):
    print(' ' * (M - i) + '*'*i)

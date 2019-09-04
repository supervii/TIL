import sys; sys.stdin = open('5356.txt', 'r')
from itertools import zip_longest
T = int(input())
for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    res = list(zip_longest(*words))
    print('#{}'.format(tc), end=' ')
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j]:
               print(res[i][j], end='')
    print()


import sys
sys.stdin = open('sw4836.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sq_li = [list(map(int,input().split())) for _ in range(N)]
    arr = [[0]*10 for _ in range(10)]
    count = 0

    for sq in sq_li:
        for x in range(sq[0], sq[2] + 1):
            for y in range(sq[1], sq[3] + 1):
                arr[x][y] += sq[4]

    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] > 2:
                count += 1


    print('#{} {}'.format(tc, count))



import sys;
sys.stdin = open('bomber5.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    # print(arr)
    for _ in range(M):
        r, c = map(int, input().split())
        for i in range(N):
            for j in range(N):
                res += arr[r][i] + arr[j][c]
                arr[r][i] = arr[j][c] = 0


    print('#{} {}'.format(tc, res))





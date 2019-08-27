import sys;
sys.stdin = open('bomber3.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    S = 0
    arr2 =[0]*3
    for i in range(N -M +1):
        for j in range(N - M +1):
            for r in range(i, i+M):
                for c in range(j, j+M):
                    S += arr[r][c]
                    if arr2[2] <= S:
                        arr2[0], arr2[1], arr2[2] = r-(M-1), c-(M-1), S
            S = 0

    print('#{} {}'.format(tc, ' '.join(map(str,arr2))))






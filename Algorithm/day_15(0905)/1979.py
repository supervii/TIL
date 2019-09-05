import sys; sys.stdin = open('1979.txt','r')
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    count = 0

    for i in range(N):
        r_sum = c_sum = 0
        for j in range(N):
            if arr[i][j]:
                r_sum += 1
            else:
                count += (r_sum == K)
                r_sum = 0
            if arr[j][i]:
                c_sum += 1
            else:
                count += (c_sum == K)
                c_sum = 0
        count += (c_sum == K) + (r_sum == K)
    print('#{} {}'.format(tc, count))
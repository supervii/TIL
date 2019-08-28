import sys; sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map = [list(input()) for _ in range(N)]

    type = {'A': 2, 'B': 3, 'C': 4}
    for i in range(N):
        for j in range(N):
            if map[i][j] != 'X' and map[i][j] !='H':
                for k in range(1, type[map[i][j]]):
                    #동
                    if j +k < N and map[i][j+k] =='H':
                        map[i][j+k] = 'X'
                    #서
                    if j -k >= 0 and map[i][j-k] =='H':
                        map[i][j-k] = 'X'
                    #남
                    if i +k < N and map[i+k][j] =='H':
                        map[i+k][j] = 'X'
                    #북
                    if i -k >= 0 and map[i-k][j] =='H':
                        map[i-k][j] = 'X'
    ans = 0
    for i in range(N):
        for j in range(N):
            if map[i][j] == 'H':
                ans += 1

    print('#{} {}'.format(tc, ans))

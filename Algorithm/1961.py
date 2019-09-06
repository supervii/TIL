import sys; sys.stdin=open('1961.txt','r')
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    print('#{}'.format(tc))
    for x in range(0,N):
        res, res2, res3 = '', '', ''
        for y in range(0,N):

            res += arr[N - y - 1][x]
            res2 += arr[N - x - 1][N - y - 1]
            res3 += arr[y][N - x - 1]

        print(res,res2,res3)

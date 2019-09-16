import sys; sys.stdin =open('5188.txt','r')

T = int(input())
dx = [0,1]
dy = [1,0]
for tc in range(1,T+1):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chk = [[10000]*N for _ in range(N)]
    chk[0][0]= arr[0][0]
    # print(chk)
    # print(arr)
    for x in range(N):
        for y in range(N):
            for i in range(2):
                tx, ty = x+dx[i], y+dy[i]
                if tx < N and ty < N:
                    num = chk[x][y] + arr[tx][ty]
                    if chk[tx][ty] > num:
                        chk[tx][ty] = num
    print('#{} {}'.format(tc,chk[-1][-1]))


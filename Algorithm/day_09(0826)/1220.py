import sys; sys.stdin = open('1220.txt','r')
for tc in range(1,11):
    N = int(input())
    mag_li = [list(map(int, input().split())) for _ in range(N)]
    arr = [[]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        data = 0
        for j in range(N):
            if mag_li[j][i] == 1:
                data = 1
            if mag_li[j][i] == 2 and data == 1:
               data = 0
               cnt += 1

    print('#{} {}'.format(tc, cnt))









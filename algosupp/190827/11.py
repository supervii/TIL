import sys; sys.stdin = open('1.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    pan = [[0]* M for _ in range(N)]
    for i in range(K):
        x1, y1, x2, y2, d = map(int, input().split())
        draw = True
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if pan[x][y] > d:
                    draw = False
        if not draw: continue
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                pan[x][y] = d

    cnt = [0] *11
    for x in range(N):
        for y in range(M):
            cnt[pan[x][y]] += 1
    print('#{} {}'.format(tc, max(cnt)))

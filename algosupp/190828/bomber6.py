import sys; sys.stdin = open('bomber6_input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for _ in range(M):
        r, c, d = map(int, input().split())
        ans += arr[r][c]
        arr[r][c] = 0

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = r, c
            for i in range(d):
                x, y = x + dx, y + dy
                if x < 0 or x >= N or y < 0 or y >= N: break
                ans += arr[x][y]
                arr[x][y] = 0

    print('#{} {}'.format(tc, ans))

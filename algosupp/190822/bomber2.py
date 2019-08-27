import sys
sys.stdin = open('bomber1.txt', 'r')
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr =[list(map(int, input().split())) for _ in range(N)]
#     res = [0]*3
#     #x= 행 ,y = 열
#     dx =[-1, -1, 1, 1] #좌상단, 우상단, 좌하단, 우하단
#     dy= [-1, 1, -1, 1]
#     ans = x = y = 0
#     for r in range(N):
#         for c in range(N):
#             # 네 방향에 대해서 자료를 읽는다.
#             S = 0
#             for i in range(4):
#                 x, y = r +dx[i], c+dy[i]
#                 while x >= 0 and x < N and y>= 0 and y <N:
#                     S += arr[x][y]
#                     x, y = x+ dx[i], y+ dy[i]
#                 S += arr[r][c]
#                 if S >= ans:
#                     ans, x, y = S, r, c

            # x, y = r - 1, c - 1
            # while x >= 0 and x < N and y >= 0 and y < N:
            #     S += arr[x][y]
            #     x, y = x - 1, y - 1
            #
            # x, y = r - 1, c + 1
            # while x >= 0 and x < N and y >= 0 and y < N:
            #     S += arr[x][y]
            #     x, y = x - 1, y + 1
            #
            # x, y = r + 1, c - 1
            # while x >= 0 and x < N and y >= 0 and y < N:
            #     S += arr[x][y]
            #     x, y = x + 1, y - 1
            #
            # x, y = r + 1, c + 1
            # while x >= 0 and x < N and y >= 0 and y < N:
            #     S += arr[x][y]
            #     x, y = x + 1, y + 1
            #
            # S += arr[r][c]
            # if S >= ans:
            #     ans, x, y = S, r, c
    #
    # print(x, y, ans)


    #
    #
    # for x in range(len(arr)):
    #     for y in range(len(arr[0])):
    #         # tx = x
    #         # ty = y
    #         # tx = res[0]
    #         # ty = res[1]
    #         cnt = 0
    #         while tx < 0 or tx == N or ty < 0 or ty == N:
    #             tx -= 1
    #             ty -= 1
    #             cnt += arr[tx][ty]
    #
    #         tx = x
    #         ty = y
    #
    #
    #         while tx < 0 or tx == N or ty < 0 or ty == N:
    #             tx += 1
    #             ty -= 1
    #             cnt += arr[tx][ty]
    #         tx = x
    #         ty = y
    #         while tx < 0 or tx == N or ty < 0 or ty == N:
    #             tx -= 1
    #             ty += 1
    #             cnt += arr[tx][ty]
    #         tx = res[0]
    #         ty = res[1]
    #         while tx < 0 or tx == N or ty < 0 or ty == N:
    #             tx += 1
    #             ty += 1
    #             cnt += arr[tx][ty]
    #         cnt += arr[x][y]
    #         print(cnt, end=' ')
    #         if res[2] <= cnt:
    #             res[2],res[0],res[1] =cnt, x, y
    #
    # print(res)
    #


dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Max = a = b = 0

    for x in range(N):
        for y in range(N):
            S = arr[x][y]
            for i in range(4):
                tx, ty = x + dx[i], y + dy[i]

                while tx >= 0 and tx != N and ty >= 0 and ty != N:
                    S += arr[tx][ty]
                    tx, ty = tx + dx[i], ty + dy[i]

            if S >= Max:
                Max, a, b = S, x, y

    print('#{} {} {} {}'.format(tc, a, b, Max))

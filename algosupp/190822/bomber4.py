import sys; sys.stdin= open('bomber4.txt', 'r')
T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # bomb_li = [list(map(int, input().split())) for _ in range(M)]
    # test = [[0]*N for _ in range(N)]
    S = 0

    for _ in range(M):
        x, y, r = map(int, input().split())

        xend = min(x + r, N)
        yend = min(y + r, N)
        for i in range(x, xend):
            for j in range(y, yend):
                S += arr[i][j]
                arr[i][j] = 0
    print('#{} {}'.format(tc, S))






    #     for i in range(N-n[2]+1):
    #         for j in range(N-n[2]+1):
    #             for x in range(n[0], n[0]+n[2]):
    #                 for y in range(n[0], n[1]+n[2]):
    #                     # test[x][y] = arr[x][y]
    #                     S += arr[x][y]
    #                     # print(S)
    #             #         if test[x][y]:
    #             #             D += arr[x][y]
    #             #             arr2[0],arr2[1] = S, D
    #             # S = 0
    #             # D = 0
    # print(arr2)

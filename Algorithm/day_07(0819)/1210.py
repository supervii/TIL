import sys
sys.stdin= open('1210.txt','r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]
    ladder_list = [[0]*100 for _ in range(100)]
    # S = []
    # for j in range(100):
    #     for k in range(100):

    # x, y = 99, 0
    # for i in range(100):
    #     if arr[99][i] == 2:
    #         y = i
    #         break
    # dir = 0
    # while x: # x == 0이면 종료
    #     if dir != 2 and y - 1 >=0 and arr[x][y-1]: # 왼쪽
    #         y, dir = y -1, 1
    #     elif dir != 1 and y +1 < 100 and arr[x][y+1]: # 오른쪽
    #         y, dir = y +1 ,2
    #     else:
    #         x, dir = x -1 ,0
    #
    # print(y)

    x, y = 99, 0
    for i in range(100):
        if arr[99][i] == 2:
            y = i
            break
    dir = 0
    while x:  # x == 0이면 종료
        if y -1 >= 0 and arr[x][y-1]:
            while y -1 >= 0 and arr[x][y-1]:
                y -= 1
            x -= 1
        elif y+1 < 100 and arr[x][y+1]:
            while y + 1 < 100 and arr[x][y+1]:
                y += 1
            x -= 1
        else:
            x -= 1

    print(y)


#     #재귀호출
# def DFS(x,y):
#     if x ==  0: return y
#
#     arr[x][y] =0
#     if y -1 >= 0 and arr[x][y-1]:
#         return DFS(x,y -1)
#     elif y +1 < 100 and arr[x][y+1]:
#         return DFS(x,y+1)
#     else:
#         return (DFS(x-1, y))

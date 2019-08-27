
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]






















import sys

sys.stdin = open("1209.txt", "r")



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    T = int(input())
    arr =[]
    M_max = 0
    heng, yul, across, across2 = 0, 0, 0, 0
    for i in range(100):
        arr.append(list(map(int,input().split())))


    # N, M = len(arr), len(arr[0])
    #
    # for j in range(N):
    #     across += arr[j][j]
    #     across2 += arr[j][99-j]
    #     for k in range(M):
    #         heng += arr[j][k]
    #         yul += arr[k][j]
    #     M_max = max(heng,yul,M_max)
    #     heng, yul = 0, 0
    #
    # M_max = max(M_max, across, across2)
    #
    #
    # print('#{} {}'.format(test_case, M_max))
    #




    for x in range(len(arr)):
        across += arr[x][x]
        across2 += arr[x][99-x]
        for y in range(len(arr[0])):
            heng += arr[x][y]
            yul += arr[y][x]
        M_max = max(heng,yul,M_max)
        heng, yul = 0, 0
    M_max= max(M_max,across, across2)

    print('#{} {}'.format(test_case, M_max))

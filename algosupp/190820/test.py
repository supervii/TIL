import sys;
sys.stdin = open('bomber1.txt', 'r')

T =int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr = []
    # for i in range(N):
    #     arr.append(list(map(int, input().split())))

    # 행 우선 순회
    # 모든 자료의 합
    total = 0
    ans = 10000000
    row_sum = col_sum = 0
    X, Y = [], []
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        ans = min(ans, row_sum, col_sum)
    print(ans, end=' ')

    S = 0
    for i in range(N): # 좌상단 -> 우하단
        S += arr[i][i]
    ans = min(ans, S)

    SS = 0
    for i in range(N): #우상단 -> 좌하단
        SS += arr[i][N-1-i]
    ans = min(ans, SS)


    #     X.append(row_sum)
    #     Y.append(col_sum)
    # a = 100000000000000
    # for a in range(len(X)):
    #     for b in range(len(Y)):
    #         result = X[a]+Y[b] -arr[a][b]
    #         if a >= result:
    #             a = result
    #
    # print(result)




T =int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 모든 M * M의 영역 좌상단 좌표를 만든다
    for i in range(N - M +1):
        for j in range(N - M +1):
            # 좌상단 i,j 가로세로 길이 = M 사각영역을 우선 탐색
            for r in range(i, i+M): # i~ i +M -1
                for c in range(j, j+M): # j~ j +M -1
                    arr[r][c]
import sys;
sys.stdin = open('bomber1.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]
    A, B = len(arr), len(arr[0])
    MX, MY = 0, 0
    X, Y = [], []
    for x in range(A):
        for y in range(B):
            MX += arr[x][y]
            MY += arr[y][x]
        X.append(MX)
        Y.append(MY)
        MX = 0
        MY = 0
    arr2 = [0]*3
    for i in range(len(X)):
        for j in range(len(Y)):
            result = X[i]+Y[j] - arr[i][j]
            if arr2[2]<= result:
                arr2[2],arr2[0],arr2[1]= result,i,j

    print('#{} {}'.format(tc, ' '.join(map(str,arr2))))


    ans = x = y = 0
    for r in range(N):
        for c in range(N):
            S = 0
            for i in range(N):
                S += arr[r][i]+ arr[i][c]
            S -= arr[r][c]
            if S >= ans:
                ans, x, y =S, r, c

    print(ans)
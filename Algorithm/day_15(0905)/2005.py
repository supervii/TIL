T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(1,N+1):
        arr += [[1]*i]

    for i in range(N):
        for j in range(1,i):
            if len(arr[i]) >= 3:
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(map(str, arr[i])))

        # for j in arr[i]:
        #     print(j, end=' ')
        # print()





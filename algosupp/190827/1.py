import sys; sys.stdin =open('1.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    check =[[0]*N for _ in range(M)]
    cnt = 0
    data = [0]*11

    for s in range(K):
        res =True
        for i in range(arr[s][1], arr[s][3]+1):
            for j in range(arr[s][0], arr[s][2]+1):
                if check[i][j] > arr[s][4]:
                    res = False
                if res == False :
                    break
        if res == True:
            for i in range(arr[s][1], arr[s][3]+1):
                for j in range(arr[s][0], arr[s][2]+1):
                #     # if check[i][j] < arr[s][4]:
                    check[i][j] = arr[s][4]

    total = 0
    max_total = 0
    for i in arr:
        total = 0
        for x in check:
            total += x.count(i[4])
        max_total = max(max_total, total)
    total = 0
    for x in check:
        total += x.count(0)
    max_total = max(max_total, total)




    print('#{} {}'.format(tc,max_total))

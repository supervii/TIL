T = int(input())
for tc in range(1,T+1):
    N = int(input())
    check = [[]*101]

    for i in range(10000):
        for j in range(10000):
            S = 0
            check = [[] * 101]
            for r in range(N):
                x, y, d, e = map(int, input().split())
                if d == 0:
                    tx, ty = x -1, y
                    check[r].append(tx)
                    check[r].append(ty)
                    continue
                if d == 1:
                    tx, ty = x + 1, y
                    check[r].append(tx)
                    check[r].append(ty)
                    continue
                if d == 2:
                    tx, ty = x, y -1
                    check[r].append(tx)
                    check[r].append(ty)
                    continue
                if d == 3:
                    tx, ty = x, y +1
                    check[r].append(tx)
                    check[r].append(ty)
                    continue
                if check[r] not in check: continue
                else:
                    S += e
                    En = S
                    tx=ty=0

    print('#{} {}'.format(tc, En))


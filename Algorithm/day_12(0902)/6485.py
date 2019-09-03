import sys; sys.stdin = open('6485.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stop = [int(input()) for __ in range(P)]
    cnt = [0]*5000
    res = []

    # print(bus)

    for i in range(N):
        # print(bus[i])
        for j in range(bus[i][0]-1,bus[i][1]):
            cnt[j] +=1

    for i in bus_stop:
        res.append(cnt[i-1])
    # print(res)



    print('#{} {}'.format(tc,' '.join(map(str,res))))







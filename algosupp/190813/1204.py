import sys
sys.stdin = open("1204.txt", "r")


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    score = list(map(int, input().split()))
    res = [0]*101
    for val in score:
        res[val] = res[val] + 1
    #print(res)

    MaxIdx = 0
    for i in range(1, len(res)):
        if res[MaxIdx] <= res[i]:
            MaxIdx = i
    print('#{} {}'.format(tc, MaxIdx))

import sys
sys.stdin = open("4865.txt", "r")

T = int(input())
for tc in range(1,T+1):
    word = set(input())
    words= list(input())
    # print(words)
    res = {}
    for i in word:
        for j in words:
            if i not in res:
                res[i] = 0
            if i == j:
                res[i] += 1

    print('#{} {}'.format(tc,max(res.values())))




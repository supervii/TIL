import sys; sys.stdin = open('1240.txt','r')
passcd = {0:'0001101',1:'0011001',2:'0010011',3:'0111101',4:'0100011',5:'0110001',6:'0101111',7:'0111011',8:'0110111',9:'0001011'}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    chk = []

    for i in range(N):
        for j in range(M-6):
            for x in range(10):
                if arr[i][j:j+7] == passcd.get(x):
                    chk = []
                    for y in range(j, M, 7):
                        for c in range(10):
                            if arr[i][y:y + 7] == passcd.get(c):
                                chk.append(c)
                    if len(chk) == 8:
                        break
                if len(chk) == 8:
                    break
            if len(chk) == 8:
                break
        if len(chk) == 8:
            break
    S = []
    mul = []
    for idx,val in enumerate(chk):
        if idx == 0 or idx%2==0:
            mul.append(val)
        else:
            S.append(val)
    # print(sum(S) + sum(mul)*3)
    if not (sum(S) + sum(mul)*3 )% 10:
        print('#{} {}'.format(tc,sum(S) + sum(mul)))
    else:
        print('#{} 0'.format(tc))



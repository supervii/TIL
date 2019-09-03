import sys; sys.stdin = open('5110.txt', 'r')
T = int(input())

for tc in range(1):
    N, M = list(map(int, input().split()))
    total= []

    for i in range(2):
        seq = list(map(int, input().split()))
        if not total:
            total = seq
        else:
            # print(total)
            for idx, j in enumerate(total):
                if seq[0] < j:
                    for k in seq:
                        total.insert(idx, k)
                        idx += 1
                    break
            else:
                for k in seq:
                    total.append(k)
                # print('초과 토탈',total)

    # print(total)
    print('#{} '.format(tc),end='')
    for i in range(len(total)-1,len(total)-11, -1):
        print(total[i],end=' ')
    print()




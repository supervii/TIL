import sys; sys.stdin = open('6190.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    res = 0
    chk =[]

    for i in range(N):
        for j in range(i+1, N):
           res = arr[i]*arr[j]
           # res = 12343
           check = str(res)
           for c in range(len(check)-1):
               if check[c] > check[c+1]:
                   break

           else:
                chk.append(res)

    if not chk:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc,max(chk)))


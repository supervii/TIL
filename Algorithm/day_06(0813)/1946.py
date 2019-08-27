import sys
sys.stdin = open("1946.txt", "r")

T = int(input())
for tc in range(1, T+1):
    res = ''
    N = int(input())
    for _ in range(N):
        arr =input().split()
        res += arr[0]*int(arr[1])

    for _ in range(len(res)):
        print(res[_], end='')
        if (_+1)%10==0:
            print()
    print()

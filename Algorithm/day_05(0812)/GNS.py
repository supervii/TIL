import sys

sys.stdin = open("GNS.txt", "r")



T = int(input())
arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for test_case in range(1, T + 1):
    N = input()
    # print(N)
    arr_li = list(map(str,input().split()))
    # print(arr_li)
    result = []
    for i in arr:
        result += [i] * arr_li.count(i)

    print('#{} {}'.format(test_case, ' '.join(result)))


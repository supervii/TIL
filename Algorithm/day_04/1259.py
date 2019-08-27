import sys

sys.stdin = open("1259.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    screw_li = list(map(int, input().split()))
    result = []
    for i in range(1, len(screw_li), 2):
        result.append([screw_li[i-1],screw_li[i]])
    # print(result)
    for j in result:








import sys

sys.stdin = open("4837.txt", "r")

T = int(input())
A = list(range(1,13))
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # print(N, K)
    AL = len(A)
    # print(AL)
    result = []
    count = 0
    for i in range(1,1 << AL):
        for j in range(AL):
            if i & (1 << j):
                result.append(A[j])


        if len(result) == N and sum(result) == K:
            count += 1
        result =[]



    print('#{} {}'.format(test_case, count))






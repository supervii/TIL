import sys
sys.stdin = open('4835.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Max = 0
    res = 0
    for i in range(N-M+1):
        for j in range(i, i+M):
            res += arr[j]
            if i == 0:
                Min = res
        if Max < res:
            Max = res
        elif Min > res:
            Min = res
        res = 0
    print('#{} {}'.format(tc, Max-Min))

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     Sum = 0
#     for i in range(M):
#         Sum += arr[i]
#     print(Sum)
#
#     Min = Max = Sum
#     for i in range(N - M + 1):
#         Sum += (arr[i + M] - arr[i])
#         MIn = min(Min, Sum)
#         Max = max(Max, Sum)
#
#     print('#{} {}'.format(test_case, Max - Min))
#
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     Min = 1000000
#     Max = 0
#
#     for start in range(N - M + 1):
#         sum = 0
#         for i in range(M):
#             sum += arr[start + i]
#
#         Min = min(Min, sum)
#         Max = max(Max, sum)
#
#     print("#%d %d" % (test_case, Max - Min))
#


# N, M = 4, 5
# arr = [[0]*M for _ in range(N)]
# num = 1
# for i in range(N):
#     for j in range(M):
#         arr[i][j] = num
#         num += 1
# print(arr)
#
# for i in range(N):
#     for j in range(M):
#         if i%2==0:
#             print(arr[i][j], end=' ')
#         else:
#             print(arr[i][M-1-j], end=' ')
#
#     print()
#


# for case in range(10):
#     n = int(input())
#     num_list = list(map(int, input().split())
#     for count in range(n+1):
#         mx, mn = 0, 0
#         for i in range(1, len(num_list)):
#             if num_list[mx] < num_list[i]:
#                 mx = i
#             if num_list[mn] > num_list[i]:
#                 mn = i
#         num_list[mx] -= 1
#         num_list[mn] += 1
#     print('#{} {}'.format(case+1, abs(mx-mn)))


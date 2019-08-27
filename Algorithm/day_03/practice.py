# N = 10
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for x in range(N):  # 모든행에 대해서
#     for y in range(N): # 모든 열에 대해서
#         # [x][y]
#         for i in range(4):
#             tx, ty = x +dx[i], y + dy[i]
#             # 경계 체크
#             if tx < 0 or tx == N or ty < 0 or ty == N: continue
#         print(tx+ty)
#
#


# arr = [[9, 20, 2, 18, 11],
# [19, 1, 25, 3, 21],
# [8, 24, 10, 17, 7],
# [15, 4, 16, 5, 6],
# [12, 13, 22, 23, 14]]
#
# N, M = len(arr), len(arr[0])
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# Sum = 0
# for x in range(N):
#     for y in range(M):
#         for i in range(len(dx)):
#             tx, ty = x +dx[i], y+dy[i]
#             if tx < 0 or ty < 0 or tx == len(arr) or ty == len(arr[0]):
#                 continue
#             val = arr[x][y] - arr[tx][ty]
#             Sum += (-val if val < 0 else val)
#
# print(Sum)



# arr = [[ 1,  2,  4,  7, 11],
#     [ 3,  5,  8, 12, 15],
#     [ 6,  9, 13, 16, 18],
#     [10, 14, 17, 19, 20]]
#
#
# N, M = len(arr), len(arr[0])
# for diag in range(0, N + M - 1):    # diag: 사선의 수
#                                     # x, y: 시작 좌표
#     x = 0 if diag < M else (diag - M + 1)
#     y = diag if diag < M else M - 1
#
#     while x < N and y >= 0:
#         print('%2d ' % arr[x][y], end='')
#         x += 1
#         y -= 1
#     print()
#
# N = 4
# bit = [0] * N
#
# for i in range(2):
#     bit[0] = i
#     for i in range(2):
#         bit[1] = i
#         for i in range(2):
#             bit[2] = i
#             for i in range(2):
#                 bit[3] = i
#                 print(bit)
#

# arr = 'abc'
# bits = [0]*3
# def print_set(bits):
#     print(bits, end=' ')
#     for i in range(len(bits)):
#         if bits[i]:
#             print(arr[i], end=' ')
#     print()
#
#
# num =10
# num2 = 0b1010
# num3 = 0xa
# print(num, num2, num3)
#
# a= 0b1010
# b= 0b1011
# c= a|b
# print(bin(c))

# a = 10
# b = a & 1 #마지막 비트가 1인지 0인지 확인하는 방법
# print(b)


# a = 0b1010
# print(a >> 1, a >> 2 )

# arr = [3, 6, 7, 1, 5, 4]
# N = len(arr)
#
# for subset in range(1 << N):
#     print(subset, end='> ')
#     for j in range(N):
#         if subset &(1 << j):
#             print(arr[j], end=' ')
#     print()
# #
arr = [3, 6, -2, 7, -3, 1, -5, -1, 5, 4]
N = len(arr)
z_sum = []
count = 0

for i in range(1,1 << N):
    # print(i, end=' ')
    for j in range(N):
        # print(j)
        if i &(1 << j): # arr[j]를 포함하는지
            z_sum.append(arr[j])
    if sum(z_sum) == 0:
        count +=1
        print(count, z_sum)
    z_sum =[]

# arr = []
# key =123
#
# def binary_search(arr, key):
#     lo, hi = 0, len(arr) - 1
#
#     while lo <= hi:
#         mid = (lo+hi) >> 1
#         if arr[mid] == key:
#             return mid
#         if arr[mid] > key:
#             hi = mid - 1
#         else:
#             lo = mid + 1
#
#     return  -1
#
#


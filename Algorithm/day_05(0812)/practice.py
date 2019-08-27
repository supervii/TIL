# T = int(input())
# for test_case in range(1,T+1):
#     words = list(input())
#     if words == words[::-1]:
#         print('{} 1'.format(test_case))
#     else:
#         print('{} 0'.format(test_case))
#
#
# arr= '12345'
# val = int(arr)

# 부루트 포스
# p = 'abcdabcef'
# t = 'asdsakllfaklabcdabcefasmdksaogkaskjidsjkf'
#
# n, m = len(t), len(p)
#
# for i in range(n -m +1):
#     for j in range(m):
#         if t[i+j] != p[j]:
#             break
#     else:
#         print(t[i:i +m])
#
#
#
# for i in range(n - m + 1):
#     j = 0
#     while j < m:
#         if t[i + j] != p[j]:
#             break
#         j += 1
#     if j ==m:
#         print(t[i:i + m])
#
#
# i = j = 0
# while i < n:
#     if p[j] != t[i]:
#         i = i - j
#         j = - 1
#     i, j = i + 1 , j + 1
#     if j == m:
#         print(t[i -j:])


# 재귀함수 - 자기 자신을 호출하는 함수
# 재귀 호출 ----> 재귀적 정의(점화식) 구현하기 위해
 # 그래프의 깊이 우선탐색, 백트래킹 / 반복

# for i in range(3):
#     print('Hello')
#

cnt = 0
def printHello(i, n):
    global cnt
    if i == n:
        cnt +=1
        print('----------------')
        return
    else:
        print(i, '>Hello')
        printHello(i+1, n)
        printHello(i + 1, n)



printHello(0, 3)
print(cnt)




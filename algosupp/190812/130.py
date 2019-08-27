# N = int(input())
# for i in range(N):
#     print('JUNGOL')
# while 문 수식(변수를 포함) , true 반복 종료 선언
# 수식에 사용되는 초기값 설정
# N = int(input())
# i = 0
# while i < N:
#     print('JUNGOL')
#     # 수식에 사용된 변수의 값을 변경
#     i += 1
#
# # break
# for i in range(5):
#     for j in range(5):
#         for k in range(5):
#             if k>j:
#                 break #감싸고 있는 for 문을 빠져나감
#
#         if j > i:
#             break
#

for i in range(5):
    print(i)
    if i == 5:
        break
else:
    print('else...')
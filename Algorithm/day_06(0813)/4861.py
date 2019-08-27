# import sys
# sys.stdin = open("4861.txt", "r")
# T = int(input())
# for tc in range(1,T+1):
#     a,b = map(int, input().split())
#     words = [input() for _ in range(a)]
#     # print(words)
#     for i in range(a): #줄
#         # print(i)
#         for j in range(a-b+1):
#             # print(i)
#             x, y = '', ''
#             for k in range(j,j+b):
#                 # print(k)
#                 x += words[i][k]
#                 y += words[k][i]
#             # print(x,x[::-1])
#             if x == x[::-1]:
#                 print('#{} {}'.format(tc, x))
#             if y == y[::-1]:
#                 print('#{} {}'.format(tc, y))
#


# 회문 조사 방법
# 가능한 모든 경우를 조사하는 방법
# for i in range(M//2):
#     if arr[s+i] != arr[e -i]:
#         break
#     else:
#         # 회문찾음
arr =[
'CBBCBAAB',
'CCCBABCB',
'CAAAACAB',
'BACCCCAC',
'AABCBBAC',
'ACAACABC',
'BCCBAABC',
'ABBBCCAA']
N = 8
M = 4
for row in range(N):
    for start in range(N- M +1):
        end = start + M -1
        for i in range(M//2):
            if arr[row][start+i] != arr[row][end-i]:
                break
        else:
            print(arr[row][start:start+M])

        # for i in range(M//2):
        #     if arr[start+i][row] != arr[end-i][row]:
        #        break
        # else:
        #     print(arr[start][row],arr[end][row])
        #
        #
for row in range(N):
    for start in range(N- M +1):
        end = start + M -1
        for i in range(M//2):
            if arr[start+i][row] != arr[end-i][row]:
                break
        else:
            ans = ''
            for col in range(start, end + 1):
                ans += arr[col][row]
            print(ans)

for tc in range(1,11):
    N=int(input())
    arr = [input() for _ in range(8)]
    ans = 0
    for idx in range(8):
        # 한행에 대해서
        for s in range(8 -N + 1):
            e = s + N - 1
            for i in range(N//2):
                if arr[idx][s+i] != arr[idx][e-i]: break
            else:
                ans += 1
            for i in range(N // 2):
                if arr[s + i][idx] != arr[e - i][idx]: break
            else:
                ans += 1
    print(ans)

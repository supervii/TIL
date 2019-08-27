import sys
sys.stdin = open("1216.txt", "r")


# for tc in range(1,11):
#     N = int(input())
#     words = [input() for _ in range(100)]
#     res = 0
#     for row in range(100):
#         for i in range(100):
#             for start in range(100-i+1):
#                 end = start + i -1
#                 for j in range(i//2):
#                     if words[row][start+j] != words[row][end-j]:
#                         break
#                 else:
#                     res = max(len(words[row][start:start+i]), res)
#                 for j in range(i // 2):
#                     if words[start + j][row] != words[end - j][row]:
#                         break
#                 else:
#                     ans = ''
#                     for col in range(start, end + 1):
#                         ans += words[col][row]
#                     res = max(len(ans),res)
#     print('#{} {}'.format(tc,res))
#

for tc in range(1,11):
    N = int(input())
    arr = [input() for _ in range(100)]
    ans = 1

    for idx in range(100):
        for s in range(100):
            for e in range(99, s , -1):
                L = e - s + 1
                if ans >= L: break
                for i in range(L//2):
                    if arr[idx][s+i] != arr[idx][e-i]:break
                else:
                    ans = L

                for i in range(L // 2):
                    if arr[idx][s + i] != arr[idx][e - i]: break
                else:
                    ans = L
    print(ans)
import sys; sys.stdin = open('1493.txt','r')
# def find_po(n):
#     i = 1
#     while i**2 -(i-2) //2 <= n:
#         i += 1
#     i -=1
#     s = (i**2 -(i-2) //2)
#     x,y = 1+(n-s), i+(n-s)
#     return (x,y)
# print(find_po(10))
res = [(0,0)]
for x in range(1,10001):
    y = 1
    while x != 0:
        res.append((y,x))
        x -= 1
        y += 1
# print(res)

T = int(input())
for tc in range(1,T+1):
    p,q = map(int, input().split())
    print('#{} {}'.format(tc,res.index((res[p][0]+res[q][0], res[p][1]+res[q][1]))))






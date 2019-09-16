# arr = [9, 2, 3, 7, 5, 6, 8, 1, 4, 10]
#
# def getMin(s,e):         #최소값 구하기
#     if s == e:
#         return arr[s]
#     else:
#         ret = getMin(s, e-1)     # 매개변수 => 문제의 크기, 반환값 =>
#         return min(ret, arr[e])
#         # #분할 탐색
#         # mid = (s+e)//2
#         # l = getMin(s, mid)
#         # r = getMin(mid+1,e)
#         # return min(l,r)
#
#
# print(getMin(0, len(arr)-1))


# 재귀 호출
#  1. 동적 계획법(DP) / 분할정복 ==> 재귀적 정의 구현할 때
#                                       - 부분문제간의 관계(큰문제와 작은문제간 관계)
# 2. 탐색
#  - 그래프 깊이 우선 탐색(DFS) , 트리 순회
#  - 백트래킹 --> 상태공간 트리, 그래프


print('순열')
arr = 'ABC'
N = len(arr)
for i in range(N):
    for j in range(N):
        if i ==j:continue
        for k in range(N):
            if k ==i or k == j: continue
            print(arr[i],arr[j],arr[k])


print('조합')

arr ='ABCDE'
N = len(arr)
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1,N):
            print(arr[i],arr[j],arr[k])

print('중복조합')
arr = 'ABCDE'
N = len(arr)
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            print(arr[i], arr[j], arr[k])

print('재귀호출')
arr = [1,2,3,4]
N = len(arr)
for i in range(N):
    arr[0],arr[i]= arr[i],arr[0]
    print(arr)
    arr[0],arr[i]=arr[i],arr[0]


print('재귀호출2')
arr = [1,2,3,4]
N = len(arr)
# for i in range(N):
#     arr[0],arr[i]= arr[i],arr[0]
#     for j in range(1,N):
#         arr[1], arr[j] = arr[j], arr[1]
#         for k in range(2,N):
#             arr[2], arr[k] = arr[k], arr[2]
#             print(arr)
#             arr[2], arr[k] = arr[k], arr[2]
#         arr[1], arr[j] = arr[j], arr[1]
#     arr[0], arr[i] = arr[i], arr[0]
def perm(k):
    if k ==N:
        print(arr)
    else:
        for i in range(k,N):
            arr[k],arr[i] = arr[i],arr[k]
            perm(k+1)
            arr[k],arr[i] = arr[i],arr[k]
perm(0)


print('재귀로 조합')
def nCr(n,r):
    if n == r or r == 0: return 1
    return nCr(n-1,r-1) +nCr(n-1,r)

print(nCr(5,3))
print(nCr(10,4))



arr ='ABCDE'
N ,R = len(arr), 3
choose =[]
def comb(k,s):
    if k == R:
        print(choose)
    else:
        for i in range(s,N):
            choose.append(arr[i])
            comb(k+1, i+1)
            choose.pop()

comb(0,0)


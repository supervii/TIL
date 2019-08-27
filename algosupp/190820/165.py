# 예제를 보고 적당한 배열을 선언한 후 1행의 1열과 3열 5열을 각각 1로 초기화하고
# 나머지는 모두 0으로 초기화 한 후 2행부터는 바로 위행의 왼쪽과 오른쪽의 값을 더하여 채운 후 출력하는 프로그램을 작성하시오.
# 1 0 1 0 1
# 0 2 0 2 0
# 2 0 4 0 2
# 0 6 0 6 0
# 6 0 12 0 6


arr = [[0]*5 for _ in range(5)]
arr[0][0] = arr[0][2] =arr[0][4] =1

N, M = len(arr), len(arr[0])
# print(N, M)
dx =[-1,-1]
dy = [-1,+1]
for i in range(1, N):
    for j in range(N):
        for k in range(2):
            tx, ty = i+dx[k], j+dy[k]
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            arr[i][j] += arr[tx][ty]

for _ in range(5):
    print(' '.join(map(str,arr[_])))
print()

# print(' '.join(map(str,arr)), end=' ')

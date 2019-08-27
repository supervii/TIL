#input
# 3
# 3 7
# 15 7
# 5 2



arr = [[0]*100 for _ in range(100)]
N = int(input())
sq_li = [list(map(int, input().split())) for _ in range(N)]
count = 0
for sq in sq_li:
    for i in range(sq[0],sq[0]+10):
        for j in range(sq[1], sq[1]+10):
            arr[i][j] = 1
# print(arr)
for x in range(len(arr)):
    for y in range(len(arr[0])):
        if arr[x][y] == 1:
            count += 1
print(count)

import sys

sys.stdin = open('1209.txt', 'r')

for num in range(1, 11):
    result = 0
    # arr = []
    x_sum, y_sum, cross_sum, cross_sum2 = 0, 0, 0, 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for x in range(len(arr)):
        cross_sum += arr[x][x]
        cross_sum2 += arr[x][99 - x]
        for y in range(len(arr[0])):
            x_sum += arr[x][y]
            y_sum += arr[y][x]
        result = max(x_sum, y_sum, result)
        x_sum, y_sum = 0, 0

    result = max(cross_sum, cross_sum2, result)
    print('#{} {}'.format(num, result))



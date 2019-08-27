import sys

sys.stdin = open("4843.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr_li = sorted(list(map(int, input().split())))
    # print(arr_li[9])
    result = []
    arr = [arr_li[i] for i in range(N-1, 4, -1)]
    # print('arr',arr)
    arr2 = [arr_li[j] for j in range(N // 2 + 1)]
    # print('arr2',arr2)

    for k in range(5):
        result += arr[k], arr2[k]

    acc = ' '.join(map(str, result))
    # print('acc', acc)
    print('#{} {}'.format(test_case, acc))



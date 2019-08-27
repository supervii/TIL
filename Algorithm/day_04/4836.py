import sys

sys.stdin = open("4836.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = [[0]*10 for _ in range(10)]
    sq_num = int(input())
    sq_list =[]
    count = 0

    for _ in range(sq_num):
        sq_list += [list(map(int, input().split()))]
    # print(sq_list)

    for sq in range(len(sq_list)):
        for i in range(sq_list[sq][0], sq_list[sq][2]+1):
            for j in range(sq_list[sq][1], sq_list[sq][3]+1):
                num = sq_list[sq][4]
                if not arr[i][j]:
                    arr[i][j] += num
                else:
                    count += 1
    print('#{} {}'.format(test_case, count))


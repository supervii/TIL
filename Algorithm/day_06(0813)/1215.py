import sys
sys.stdin = open("1215.txt", "r")

for tc in range(1,11):
    num = int(input())
    # print(num)
    words = [input() for _ in range(8)]
    # print(words)
    result = 0
    for row in range(8):
        for start in range(8-num +1):
            end = start + num - 1
            for i in range(num//2):
                if words[row][start + i] != words[row][end - i]:
                    break
            else:
                result += 1

            for i in range(num//2):
                if words[start + i][row] != words[end - i][row]:
                    break
            else:
                result += 1



    # print(result)
    print('#{} {}'.format(tc, result))


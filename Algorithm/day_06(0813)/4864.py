import sys
sys.stdin = open("4864.txt", "r")

T = int(input())
for tc in range(1,T+1):
    word = input()
    words = input()
    count = 0
    if word in words:
        count +=1
    print('#{} {}'.format(tc,count))
import sys
sys.stdin = open("input.txt", "r")


#  다시 돌아온 한글 코딩
# 먼저 들어오는 데이터 값 처리는 ?  이렇게 하면 되는구나 .

N = int(input())
arr =   

# print(N, arr)
view = 0
count = 0
for k in range(10):
    for i in range(2, N-2):
        for j in range(i):
            if j >= (j-2) and (j-1) and (j+1) and (j+2):
                view += 1
    count += 1
    print('#{} {}'.format(count, view))


for n in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    for i in range(2, n-1):
        Max = max(num[i-2], num[i-1], num[i+1], num[i+2])
        if Max < num[i]:
            result += num[1]- Max
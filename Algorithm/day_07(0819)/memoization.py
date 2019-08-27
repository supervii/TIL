# 재귀적 DP (재귀호출 + 메모이제이션)
memo = [-1] * 100

def fibonacci(n):

    memo[0], memo[1] = 0, 1
    for i in range(2, n + 1): # i ==> 문제를 나타내는 값
        memo[i] = memo[i-1]  + memo[i-2]
    return memo[n]




    # if n ==1 or n == 0:
    #     return n
    # if memo[n] != -1:
    #     return memo[n]
    #
    # memo[n] = fibonacci(n-1) +fibonacci(n-2)
    # return memo[n]

print(fibonacci(40))
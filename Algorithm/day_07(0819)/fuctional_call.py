# 문제를 재귀적으로 푼다
# 재귀적 정의를 구현할 때 재귀호출이 좋다
# 재귀적 정의 --> 좀 더 작은 문제의 답을 사용해서 더 큰 문제의 답을 구하는 방법
# 팩토리얼 구하는 문제
# 문제의 크기는 자연수로 표현
# 1! =1; 2! =1!*2; 3! = 2!*3 ....; n! =(n-1)! *n

def factorial(n): # 매개변수 - 문제(크기)를 나타내는 값
                  # 반환값 - n! 의 값(문제의 해)
    if n == 0 or n == 1:
        # 재귀호출을 하지 않고 종료
        return 1
    else:
        # 재귀호출
        return factorial(n-1) * n

print(factorial(4))


def fibonacci(n): # n번째 피보나치 수를 반환
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

print('start')
print(fibonacci(35))
print('end')




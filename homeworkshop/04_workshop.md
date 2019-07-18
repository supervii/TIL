# Python 4. 함수 II

##### 양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요. 

```python
def my_sqrt(n):
    x, y = 1, n
    result = 1
    # 제곱근의 제곱과 입력 ㄱㅄ 의 차이가 적어도 이 정도 차이보다 작아지면
    while abs(result**2 - n) > 1e-10: #0.0000000001
        result = (x+y)/2 #양쪽 끝값을 더해서 2로 나눈다.
        #위 근사치에 따라 x 또는 y 의 값을 바꾼다
        if result**2 < n:
            x = result
        else:
            y = result
    return result

print(my_sqrt(2))

#    
import math
def my_sqrt(n):
    x, y = 1, n
    result = 1
    # 제곱근의 제곱과 입력 ㄱㅄ 의 차이가 적어도 이 정도 차이보다 작아지면
    while not math.isclose(result**2 - n): #0.0000000001
        result = (x+y)/2 
        if result**2 < n:
            x = result
        else:
            y = result
    return result

print(my_sqrt(2))
    
```


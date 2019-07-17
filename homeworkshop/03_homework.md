# Python 3. 함수

1. Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.

   ```python
   dir(__builtins__)
   ```

   print(), id(), list(), set(), input(), divmod(), range()........

   

2. 다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
    
   정답 ) 3 ssafy(name='허준', '구미') 키워드 인자 뒤에도 키워드 인자가 나와야함
```





3. 다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.

   ```python
   def my_func(a,b):
       c = a+b
       print(c)
       
    result = my_func(4,7)
   
   result 값은 None / jupyternote일 경우는 11
   ```

   
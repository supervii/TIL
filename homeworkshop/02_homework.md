# Python 2. 데이터구조

#### 1. 아래 보기 중, 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 구분 하시오.

String List Tuple Range Set Dictionary

mutable : List, Set, Dictionary(value)

immutable : String, Tuple, Range()



#### 2. range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.

```python
a = list(range(1,51))
b = a[0::2]
b
```



#### 3. 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.

```python
student_dict = {
    '학생이름' :'11', 
    '학생이름2':'22'
}
```


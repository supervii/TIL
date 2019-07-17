# Python 3. 함수

##### Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다.  단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.



```python
def palindrome(word): #NAN
    list_word = list(word) #['N','A','N']
    # 단어요소에 양쪽 끝끼리 계속 비교 하면서 진행
    for i in range(len(list_word)//2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True    
#2 
# word == word[::-1]
    
    

```


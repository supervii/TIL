# doc string
"""
이 함수는 ....
누가 만들
어떻게
이런 함수
"""
"""
다음과 같은 파일 quest.txt가 있다 
0
1
2
3

이파일의 내용을 다음과 같이 역순으로 reverse_quest.txt로 만들기
3
2
1
0
"""
# 읽고 뒤집고 작성하고


with open('quest.txt', 'r') as f:
    lines = f.readlines()
    for line in reversed(lines):
        # print(line.strip())

with open('reverse_quest.txt', 'w') as f:
     for line in reversed(lines):
         f.write(line)

# with open('reverse_quest.txt', 'w') as f:
#      f.writelines(reversed(lines))
# 변수에 만들고 싶은 파일을 open()해야한다 
# f = open('만들파일명', '행동')
# 행동은 r:읽기/ w:쓰기 (덮어씌워짐)/ a: 추가
f = open('ssafy.txt', 'w')
for i in range(10):
     f.write(f'This is line {i+1}.\n')
f.close()

# with 구문 (context manager)
with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'this is line {i+1}.\n')




# writelines() :list를 넣어주면 , 요소하나당 한줄씩 작성한다. 리스트를 쓰기위한 함수
# with open('ssafy.txt', 'w') as f:
#     f.writelines(['0', '1', '2', '3'])
# 밖에서 리스트선언 가능 



# 이스케이프 문자
# \n : 개행문자 (다음줄 이동 )
# \t : 텝문자
# \\ : 백슬래쉬 사용
# \' : 따옴표
# \" : 쌍따옴표
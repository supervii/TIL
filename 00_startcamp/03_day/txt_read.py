#read()
# with open('with_ssafy.txt', 'r') as f:
#     all_text = f.read()
#     print(all_text)


# readlines() : 파일의 모든 라인을 읽어서 가각의 줄을 요소로 갖는 list로 만들어 냄
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        # print(dir(line)) 관련 함수 찾아보기 
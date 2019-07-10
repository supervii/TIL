import os

# 해당 파일들이 있는 위치로 이동
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\chage_filenames')

# 현재 폴더 안에 모든 파일 이름을 수집 
filenames = os.listdir('.')

# 각각의 파일명을 돌면서 수정한다
# for filename in filenames:
#     os.rename(filename, f'SAMSUNG_{filename}')


# Samsung을 ssafy로 변환
for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG_','SSAFY_'))


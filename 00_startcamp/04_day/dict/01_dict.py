# 딕셔너리 만들기 -1 
lunch = {
    '중국집': '02-236-4545'
    }

# 딕셔너리 만들기 -2 
dinner =dict(중국집='02-236-4545', 일식집='031-424-4223')


# 딕셔너리에 내용 추가하기
lunch['분식집'] = '032-232-4624'
print(lunch)


# 딕셔너리 내용 가져오기
idol = {
    'bts':{
        '지민': 25,
        'RM': 24,
        }
    }


# RM의 나이는?
# 위의 경우는 서버가 꺼질 수 있고 아래는 none 값 반환
idol['bts']['RM']
idol.get('bts').get('RM')

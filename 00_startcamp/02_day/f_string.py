name = '신정우'

# print(f'안녕하세요, {name}입니다.')

#점심 메뉴 추천 
import random
# menu = ['찜닭','삼겹살','짜장면']
# lunch = random.choice(menu)

# print(f'오늘의 점심은 {lunch}입니다.')

# 로또 추천
numbers = range(1,46)
lotto = random.sample(numbers,6)

print(f'오늘의 행운의 로또 당첨번호는 {sorted(lotto)}입니다.')

# 필요하면 이렇게도 해보자 

print('안녕하세요,'+ name + '입니다.')

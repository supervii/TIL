avengers = [
    {
        "name": "tony stark",
        "gender": "male",
        "appearances": 3068,
        "years since joining": 52
    },
    {
        "name": "robert bruce banner",
        "gender": "male",
        "appearances": 2089,
        "years since joining": 52
    },
    {
        "name": "thor odinson",
        "gender": "male",
        "appearances": 2402,
        "years since joining": 52
    },
    {
        "name": "steven rogers",
        "gender": "male",
        "appearances": 3458,
        "years since joining": 51
    }
]

# 1.csv.DictWriter()
import csv
# # with 구문
with open('avengers.csv', 'w', newline='', encoding='utf-8') as f:
    #저정할 데이터들의 필드 이름을 미리 정한다.
    fieldnames = ('name', 'gender', 'appearances', 'years since joining')
    writer = csv.DictWriter(f, fieldnames=fieldnames) # 앞에 파란건 약속 저렇게 무조건 써야함

# 필드 이름을 csv 최상단에 작성한다. 
    writer.writeheader()

#딕셔너리를 순회하며 key를 통해 한줄씩(value를) 작성한다. 
    for avenger in avengers:
        writer.writerow(avenger)



# 2. csv.DictReader()
with open('avengers.csv','r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = ('name', 'gender', 'appearances', 'years since joining')
    #한줄씩 읽는다.
    for row in reader:
        print(row['name'])
    
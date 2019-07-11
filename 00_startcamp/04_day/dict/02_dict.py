lunch = {
    '중국집' : '02-236-4545',
    '분식집' : '02-323-4142'
}


# 기본활용
for key in lunch:
    print(key)
    print(lunch,(key))

# .items()
for key, value in lunch.items():
    print(key,value)

# value만 가져오기 
for value in lunch.values():
    print(value)

# key 만 가져오기 
for key in lunch.keys():
    print(key)
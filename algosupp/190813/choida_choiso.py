arr = [7, 4, 8, 1, 3, 5, 2, 1, 8, 6]
# 최대 최소 값
# print(max(arr),min(arr))
Min = arr[0]
for i in range(1, len(arr)):
    if Min  > arr[i]:
        Min = arr[i]
print(Min)

# 최소값의 위치 찾기
MinIdx = 0 #0번 위치를 최소 값의 위치로 저장
for i in range(1, len(arr)):
    if arr[MinIdx] > arr[i]: # 등호를 넣고 안넣고에 따라 맨 앞과 뒤의 위치를 가져올수 있다.
        MinIdx = i
print(MinIdx, arr[MinIdx])

arr = [0, 4, 1, 3, 1, 2, 4, 1]
# 값의 등장 횟수 계산
# 자료값을 리스트의 인덱스를 사용한다.
# 자료값들이 양의 정수여야 한다.
# 자료값들의 범위(최대값)를 알아야 한다.

cnt = [0]*5
for val in arr:
    cnt[val] = cnt[val] + 1
# print(cnt)

for i in range(len(cnt)):
    print(i, cnt[i])

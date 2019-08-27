

#5 6 3 4 5 5 2 2 4 6

# 1 : 0
# 2 : 2
# 3 : 1
# 4 : 2
# 5 : 3
# 6 : 2

res = [0]*6
# print(res)
N = map(int, input().split())
for i in N:
    if res[i-1] == 0:
        res[i-1] += 1
    else:
        res[i - 1] += 1



print('1 : {}'.format(res[0]))
print('2 : {}'.format(res[1]))
print('3 : {}'.format(res[2]))
print('4 : {}'.format(res[3]))
print('5 : {}'.format(res[4]))
print('6 : {}'.format(res[5]))
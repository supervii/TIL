N = int(input())
result = []
for i in range(1,101):
    if i%N ==0:
        print(i, end=' ')
        if i%10 ==0: break

# # print(result)
# # for j in result:
# #
# # print(' '.join(map(str, result)))
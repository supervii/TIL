# n = int(input())
# star_list = list(range(1,20,2))
# for star in range(n):
#         print(' '*star+ '*'*star_list[n-star-1])
# for star in range(n-1, 0, -1):
#     print(' '*(star-1)+ '*'*star_list[n-star])


M = int(input())

for i in range(1, M + 1, 2):
    print(' ' * (M - i) + '*'*i)
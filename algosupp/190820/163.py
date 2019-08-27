arr = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
Sum = 0
for i in arr:
    # print(i)
    for j in i:
        print('{} '.format(j), end='')
        Sum += j
    print()
print(Sum)

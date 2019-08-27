N = int(input())
cnt = 1
for i in range(N):
    for j in range(N):
        if i > j:
            print('  ', end='')
        else:
            print('{} '.format(cnt), end='')
            cnt += 1

    print()

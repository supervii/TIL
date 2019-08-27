N = input()
stack = []
top = -1
for i in N:
    if i.isdigit():
        print(i, end='')

    elif i == '+' or i == '-' or i == '*' or i == '/':
        top += 1
        stack.append(i)
for i in range(0, top+1):
    print(stack.pop(), end='')
print()

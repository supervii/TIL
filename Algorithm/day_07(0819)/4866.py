# 괄호
S =[]
def push(item):
    S.append(item)

def pop():
    return S.pop()

def isEmpty():
    return len(S) == 0

#
paren = '()()((()))'
for ch in paren:
    if ch == '(':
        push(ch)
    else:
        if isEmpty():
            print(0)
            break
        if ')' and pop() != '(':
            break
if isEmpty():
    print(1)
else:
    print(3)



#
#
T = int(input())
for tc in range(1,T+1):
    words = input()
    S = []
    for ch in words:
        if ch == '(' or ch == '{':
            S.append(ch)

        elif ch == ')' or ch =='}':
            if len(S) == 0:
                print(0)
                break
            if ch == ')' and S.pop() != '(':
                print(0)
                break
            if ch == '}' and S.pop() != '{':
                print(0)
                break
    if len(S) > 0:
        print('#{} 0'.format(tc))

    else:
        print('#{} 1'.format(tc))








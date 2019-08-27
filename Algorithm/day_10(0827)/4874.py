import sys; sys.stdin = open('4874.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = input().split()
    numstack = []
    opstack = []
    operator = ['*', '/', '+', '-']
    top = -1
    for i in N:
        if i not in operator:
            numstack.append(i)
        else:
            if len(numstack) < 2:
                print('#{} error'.format(tc))
                break
            else:
                right = int(numstack.pop())
                left = int(numstack.pop())
                # numstack.append(str((left + i + right)))
                if i == '+':
                    numstack.append(left+right)
                if i == '-':
                    numstack.append(left - right)
                if i == '*':
                    numstack.append(left * right)
                if i == '/':
                    numstack.append(int(left / right))




    else:
        if len(numstack) ==2:
            print('#{} {}'.format(tc, int(numstack[0])))
        else:
            print('#{} error'.format(tc))


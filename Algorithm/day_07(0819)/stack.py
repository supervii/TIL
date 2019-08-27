# C-style
S = [0] * 3 # 저장소
top = -1

def push(item):
    global top
    # full 상태를 체크
    if top == 2: return
    top += 1
    S[top] = item

def pop():
    global top
    # empty 상태 체크
    if top == -1: return
    ret = S[top]
    top -= 1
    return ret

for i in range(3):
    push(i)

print(pop())
print(pop())
print(pop())


# python-style
S =[]
def push(item):
    S.append(item)

def pop():
    return S.pop()

def isEmpty():
    return len(S) == 0


for i in range(3):
    push(i)

while not isEmpty():
    print(pop())


from collections import deque
import time
start = time.time()
S = deque()
N = 100000
for i in range(N):
    S.append(i)
while S:
    S.pop() #popleft() 들어간 순서대로 나옴
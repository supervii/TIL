import queue

# Q = []
# def enQueue(item):
#     global rear
#     if isFull():
#         print('Queue_Full')
#     else:
#         rear = rear+1
#         Q[rear] = item
#
#
#
# def deQueue():
#     if isEmpty():
#         print('Queue_Empty')
#     else:
#         front = front +1
#         Q[front]
#
# def isEmpty():
#     return front ==rear
#
# def isFull():
#     return rear == len(Q)-1
#
# def Qpeek():
#     if isEmpty():
#         print('Queue_Empty')
#     else:
#         return Q[front+1]

# 선형 큐
q =queue.Queue()
q.put('1')
q.put('2')
q.put('3')

while not q.empty():
    print(q.get())

# 원형 큐
def isEmpty():
    return front ==rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = (rear+1) % len(cQ)
        cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front +1)% len(cQ)
        return cQ[front]

cQ_SIZE = 4
cQ = [0]*cQ_SIZE
front = rear= 0
enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())
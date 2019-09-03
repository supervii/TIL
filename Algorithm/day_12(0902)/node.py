class Node:
    def __init__(self,data,link):
        self.data = data
        self.link = link


def addtoFirst(data): # 첫 노드에 삽입
    global Head
    Head = Node(data,Head) # 새로운 노드 생성


def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)


def addtoLast(data):
    global Head
    if Head ==None: #빈 리스트이면
        Head=Node(data,None)
    else:
        p = Head
        while p.link !=None: #마지막 노드를 찾을때 까지
            p = p.link
        p.link= Node(data, None)


def delete(pre): #pre 다음 노드
    if pre == None or pre.link==None:
        print('error')
    else:
        pre.link =pre.link.link

# def deleteFirst(data)


data = [1, 2, 3, 4]
Head =None

for i in range(len(data)):
    addtoFirst(data[i])
    # addtoLast(data[i])


delete(Head)

while Head.link != None:
    print(Head.data, end='->')
    Head = Head.link
print(Head.data)

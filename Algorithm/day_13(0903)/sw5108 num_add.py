import sys; sys.stdin = open('5108.txt', 'r')

class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoLast(data): #마지막 데이터 삽입
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None: #마지막 노드 찾을 때 까지
            p = p.link
        p.link = Node(data, None)

def add(pre, data): #pre 다음에 데이터 삽입, 가운데 노드로 삽입하는 알고리즘
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     seq = list(map(int, input().split()))
#     change_sq = [list(map(int,input().split())) for _ in range(M)]
#     Head = None
#
#
    #
    # for i in change_sq:
    #     seq.insert(i[0],i[1])
    #
    # print('#{} {}'.format(tc,seq[L]))
    #

T = int(input())
for tc in range(1):
    N, M, L = list(map(int, input().split()))
    sequence = list(map(int, input().split()))
    Head = None
    for i in sequence:
        addtoLast(i)


    for i in range(M):
        x, y = list(map(int, input().split()))
        insert_link = Head.link
        for j in range(x-2):
            insert_link = insert_link.link
        add(insert_link, y)
        N += 1

    result_link = Head.link
    for i in range(L-1):
        result_link = result_link.link

    print('#{} {}'.format(tc, result_link.data))




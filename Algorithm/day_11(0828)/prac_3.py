def BFS(v):
    visit[v]= True
    Q = []
    D =[v]
    print(v, end=' ')
    Q.append(v)
    while Q:
        s = Q.pop(0)
        for i in G[s]:
            if visit[i] == False:
                print(i, end=' ')
                visit[i] = True
                Q.append(i)
                D.append(i)








arr_li = [[1,2],[1,3],[2,4],[2,5],[4,6],[5,6],[6,7],[3,7]]
G = [[] for _ in range(8)]
visit = [False] * 8

for x, y in arr_li:
    G[x].append(y)

BFS(1)




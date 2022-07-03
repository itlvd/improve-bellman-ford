from inspect import stack


def relax(D, P,s,d,w):
    if D[s] != float("Inf") and D[d] > D[s] + w:
        D[d] = D[s] + w
        P[d] = s
        return True
    return False

def print_solution(Previous,dist, Point):
    print("From source")
    print("to\tprevious\tmin distance")
    for i in range(len(Point)):
        pre = Point[Previous[i]]
        if(Previous[i] == -1):
            pre = -1
        print(Point[i], '\t', pre, '\t\t\t\t', dist[i])

def printPath(s,d,P,D,Point):
    now = d
    path = ""
    while(now != s):
        path += Point[now] + ">-"
        now = P[now]
        if now == -1:
            print("Don't have solution for this path")
            return
    path += Point[s]
    print(path[::-1], "length =", D[d])

def topo(v,visited, stack, graph):
    visited[v] = True
    for edge in graph: #Lay danh sach tat ca cac canh
        if edge[0] == v: #Chi lay source vertex dang xet
            if visited[edge[1]] == False: #Dinh des chua visited thi loop o nhung dinh do, sau do bo vao stack
                topo(edge[1],visited,stack,graph)

    stack.insert(0,v)

def sortTopo(start, graph, n):
    visited = [False] * n
    stack = []

    #Swap listVertex[start] <-> listVertex[0]
    listVertex = list(range(n))
    tmp = listVertex[0]
    listVertex[0] = listVertex[start]
    listVertex[start] = tmp


    for i in listVertex: #Chay het tat ca cac diem
        if(visited[i] == False): # Chi xet nhung diem chua tham
            topo(i,visited,stack,graph) # xet canh output o dinh i

    return stack


def Yen(start, graph, n):
    D = [float("Inf")] * n
    P = [-1] * n
    D[start] = 0
    C = [start]
    topoSorting = sortTopo(start,graph,n)
    reverseTopo = topoSorting.copy()
    reverseTopo.reverse()
    FlagChange = [False] * n #Flag change iteration before 
    while len(C) > 0: 
        C_new = []
        for i, u in zip(range(len(topoSorting)),topoSorting):
            if(u in C or FlagChange[u] == True): # Co trong C hay co thay doi o vong while truoc khong
                FlagChange[u] = False
                for j, v in zip(range(len(topoSorting)),topoSorting): # G+ dam bao duyet tu trai sang phai. Chon 2 cap diem u,v xet xem co canh noi giua chung khong
                    if(u != v and j > i): # luon xet diem ben phai
                        for edge in graph:
                            if(u == edge[0] and v == edge[1]): # Check ton tai canh nay khong
                                temp = D[v]
                                relax(D,P,u,v,edge[2])
                                if(temp != D[edge[1]]):
                                    FlagChange[edge[1]] = True
                                    C_new.append(edge[1])


        for i, u in zip(range(len(topoSorting)),reverseTopo):
            if(u in C or FlagChange[u] == True): # Co trong C hay co thay doi o vong while truoc khong
                FlagChange[u] = False
                for j, v in zip(range(len(topoSorting)),reverseTopo): # G+ dam bao duyet tu trai sang phai. Chon 2 cap diem u,v xet xem co canh noi giua chung khong
                    if(u != v and j > i): # luon xet diem ben phai
                        for edge in graph:
                            if(u == edge[0] and v == edge[1]): # Check co ton tai canh nay khong
                                temp = D[v]
                                relax(D,P,u,v,edge[2])
                                if(temp != D[edge[1]]):
                                    FlagChange[edge[1]] = True
                                    C_new.append(edge[1])
        C = C_new
    
    return D, P

def convertConvex(filename):
    Point = []
    graph = []
    id_ = {}
    id_now = 0
    with open(filename) as f:
        while True:
            strx = f.readline()
            if not strx:
                break
            start = 0
            end = 0
            weight = 0
            s = 0
            d = 0
            if "->" in strx:
                index = strx.find("->")
                index2= strx.find("=")
                start = strx[:index]
                end = strx[index + 2:index2]
                weight = strx[index2+1:-1]
                w = int(weight)
                if start not in Point:
                    Point.append(start)
                    id_[start] = id_now
                    id_now += 1
                if end not in Point:
                    Point.append(end)
                    id_[end] = id_now
                    id_now += 1
                s = id_[start]
                d = id_[end]
                graph.append([s,d,w])


    return Point, graph

#============= Setup variable
begin = 6
end = 0
#=============
start = 0
des = 0 
Point, graph = convertConvex("data.txt")
n = len(Point)
for i in range(n):
    if Point[i] == str(begin):
        start = i;
    if Point[i] == str(end):
        des = i;

D, P = Yen(start,graph,n)
printPath(start,5,P,D,Point)


#Check topo sorting
# s = sortTopo(start,graph,n)
# print(Point)
# print(s)



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
        path += str(Point[now])[::-1] + ">-"
        now = P[now]
        if now == -1:
            print("Don't have solution for this path")
            return
    path += str(Point[s])[::-1]
    print(path[::-1], "length =", D[d])

def Yen(start, graph, n):
    D = [float("Inf")] * n
    P = [-1] * n
    D[start] = 0
    C = [start]
    listPoint = list(range(n)) # node
    reversePoint = listPoint.copy()
    reversePoint.reverse()

    tmp = listPoint[0] #swap
    listPoint[0] = listPoint[start]
    listPoint[start] = tmp

    visited = [False] * n #kiem tra xem node da di qua chua, neu da di qua roi, thi khong quay lai, do thu tu topo khong cho phep
    visited[start] = True
    FlagChange = [False] * n #Flag change iteration before 
    while len(C) > 0: 
        C_new = []

        for i, u in zip(range(n),listPoint):
            if(u in C or FlagChange[u] == True): # Co trong C hay co thay doi o vong while truoc khong
                FlagChange[u] = False
                for edge in graph:
                    if(u == edge[0] and visited[edge[1]] == False): # Check ton tai canh nay khong
                        visited[edge[1]] = True
                        temp = D[edge[1]]
                        relax(D,P,u,edge[1],edge[2])
                        if(temp != D[edge[1]]):
                            FlagChange[edge[1]] = True
                            #if edge[1] not in C_new: 
                            C_new.append(edge[1])
        visited = [False] * n

        for i, u in zip(range(n),reversePoint):
            if(u in C or FlagChange[u] == True): # Co trong C hay co thay doi o vong while truoc khong
                FlagChange[u] = False
                for edge in graph:
                    if(u == edge[0] and visited[edge[1]] == False): # Check ton tai canh nay khong
                        visited[edge[1]] = True
                        temp = D[edge[1]]
                        relax(D,P,u,edge[1],edge[2])
                        if(temp != D[edge[1]]):
                            FlagChange[edge[1]] = True
                            #if edge[1] not in C_new: 
                            C_new.append(edge[1])
        C = C_new
        visited = [False] * n
    
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
begin = 0
end = 244
#=============
start = 0
des = 0 
Point, graph = convertConvex("2000node.txt")
n = len(Point)
for i in range(n):
    if Point[i] == str(begin):
        start = i;
    if Point[i] == str(end):
        des = i;

D, P = Yen(start,graph,n)
#printPath(start,5,P,D,Point)
#print_solution(P,D,Point)

#Check topo sorting
# s = sortTopo(start,graph,n)
# print(Point)
# print(s)



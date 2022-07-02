def relax(D, P,s,d,w):
    if D[s] != float("Inf") and D[d] > D[s] + w:
        D[d] = D[s] + w
        P[d] = s

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



def Yen(start, graph, n):
    D = [float("Inf")] * n
    P = [-1] * n
    D[start] = 0
    C = [start]
    while len(C) > 0: 
        C_new = []
        for u in range(n):
            if(u in C or D[u] != float("Inf")): # luu y co the sai
                for v in range(n): # G+ dam bao duyet tu trai sang phai
                    if(u != v):
                        for edge in graph:
                            if(u == edge[0] and v == edge[1]): # Check co ton tai canh nay khong
                                temp = D[v]
                                relax(D,P,u,v,edge[2])
                                if(temp != D[edge[1]]):
                                    C_new.append(edge[1])


        for u in range(n-1,-1,-1):
            if(u in C or D[u] != float("Inf")):
                for v in range(n,1,-1):
                    if(u != v):
                        for edge in graph:
                            if(u ==edge[0] and v == edge[1]):
                                temp = D[v]
                                relax(D,P,u,v,edge[2])
                                if(temp != D[edge[1]]):
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
Point, graph = convertConvex("data_generate.txt")
n = len(Point)
for i in range(n):
    if Point[i] == str(begin):
        start = i;
    if Point[i] == str(end):
        des = i;

D, P = Yen(start,graph,n)
printPath(start,5,P,D,Point)




def relax(D, P,s,d,w):
    if D[s] != float("Inf") and D[d] > D[s] + w:
        D[d] = D[s] + w
        P[d] = s

def print_solution(dist, Previous, Point):
    print("Vertex Distance from Source")
    for i in range(len(Point)):
        print("{0}\t{1}\t{2}".format(Point[i], Point[Previous[i]], dist[i]))

def printPath(s,d,P,D,Point):
    now = d
    path = ""
    while(now != s):
        path += Point[now] + ">-"
        now = P[now]
    path += Point[s]
    print(path[::-1], "length =", D[d])
        



def basicBellmanFord(start,graph, n):
    D = [float("Inf")] * n
    P = [0] * n
    D[start] = 0
    for _ in range(len(D) - 1):
        for s,d,w in graph:
            relax(D,P,s,d,w)
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


def early_termination(start, graph, n):
    D = [float("Inf")] * n
    P = [0] * n
    D[start] = 0
    C = [start]
    while C!= None: 
        C_new = []
        for vertex in C:
            for edge in graph:
                if edge[0] != vertex:
                    continue
                temp = D[edge[1]]
                relax(D, P, edge[0], edge[1], edge[2])
                if temp != D[edge[1]]:
                    C_new.append(edge[1])
        if len(C_new) != 0:
            C = C_new
        else:
            C = None
    
    return D, P
    
        

Point, graph = convertConvex("data.txt")
start = 0
n = len(Point)
D, P = early_termination(start,graph,n)
printPath(start,2,P,D,Point)


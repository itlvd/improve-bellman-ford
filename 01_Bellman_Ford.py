#============= Setup variable =======================
begin = 0
end = 199
path_data = "./data_demo/data.txt"
print_shortest_path = False;
print_all_solution = True;
#====================================================

def relax(D, P,s,d,w):
    if D[s] != float("Inf") and D[d] > D[s] + w:
        D[d] = D[s] + w
        P[d] = s

def print_solution(Previous,dist, Point):
    print("From source")
    print("to\tprevious\tmin distance")
    tmp_list = []
    isnum = Point[0].isnumeric()
    for i in range(len(Point)):
        pre = Point[Previous[i]]
        if(Previous[i] == -1):
            pre = -1
        if isnum != True:
            tmp_list.append([Point[i], pre, dist[i]])
        else:
            tmp_list.append([int(Point[i]), pre, dist[i]])
    tmp_list.sort(key  = lambda x:x[0])
    for point, p, d in tmp_list:
        print("{0:10}{0:10}{1}".format(str(point),p,d))

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


def basicBellmanFord(start,graph, n):
    D = [float("Inf")] * n
    P = [-1] * n
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

start = 0
des = 0 
Point, graph = convertConvex(path_data)
n = len(Point)
for i in range(n):
    if Point[i] == str(begin):
        start = i;
    if Point[i] == str(end):
        des = i;

D, P = basicBellmanFord(start,graph,n)

if print_shortest_path == True:
    printPath(start,des,P,D,Point)
if print_all_solution == True:
    print_solution(P,D,Point)


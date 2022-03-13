#the number of vertices
vertices = 20

#defining infinity variable
INF = 99999999 

#implementation of the floyd warshall algorithm
def floyd_warshall(graph):

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    #adding vertices individually
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j] )
    result(dist)

def result(dist):
    
    print ("This matrix represents the shortest distances between every pair of vertices")
    
    for i in range(vertices):
        for j in range(vertices):
            if(dist[i][j] == INF):
                print ("%7s" % ("INF"),end=" ")
            else:
                print ("%7d\t" % (dist[i][j]),end=' ')
            if j == vertices-1:
                print ()

#Considering city 1[Rabat] as the starting point
graph = [
    [0,1063,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,30],
    [1063,0,2656,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,2650,0,1352,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,1352,0,1841,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,1841,0,61,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,61,0,1634,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,1634,0,151,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,151,0,285,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,285,0,146,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,146,0,11,INF,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,11,0,380,INF,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,380,0,2547,INF,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,2547,0,97,INF,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,97,0,6999,INF,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,6999,0,63,INF,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,63,0,105,INF,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,105,0,244,INF,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,244,0,502,INF],
    [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,502,0,30],
    [1063,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,30,0]
    ]

floyd_warshall(graph)

import sys
import math
input=sys.stdin.readline

def dfs(node):
    Visited[node]=True
    print(node,end='')
    
    for next in range(N):
        if not Visited[next] and Graph[node][next]:
            dfs(next)
            
if __name__=='__main__':
    N,E=map(int,input().split())
    Visited = [False for _ in range(N)]
    Graph = [[0 for _ in range(N)] for _ in range(N)]
    
    values = list(map(int,input().split()))
    for i in range(E):
        u,v=values[i*2],values[i*2+1]
        Graph[u][v]=Graph[v][u]=1
    print(Graph)
    dfs(0)
    
#깊이우선탐색 순서를 출력
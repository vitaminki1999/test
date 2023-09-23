import sys
import math
input=sys.stdin.readline

def dfs(node):
    visited[node]=True
    print(node,end='')
    
    for next in range(n):
        if not visited[next] and gragh[node][next]:
            dfs(next)


n,e=map(int,input().split())
visited=[False for _ in range(n)]
gragh=[[0 for _ in range(n)] for _ in range(n)]

values=list(map(int,input().split()))
for i in range(e):
    a,b=values[2*i],values[2*i+1]
    graph[a][b]=graph[b][a]=1
dfs[0]
import sys
import math
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,y):
    visited[x][y]=True
    main=gragh[x][y]
    
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if (0<=nx<n) and (0<=ny<n):
            if not visited[nx][ny]:
                if main==gragh[nx][ny]:
                    dfs(nx,ny)

n=int(input())
gragh=[list(input()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

tree_clo,two_clo=0,0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            tree_clo+=1

for i in range(n):
    for j in range(n):
        if gragh[i][j]=="G":
            gragh[i][j]="R"

visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            two_clo+=1
            
print(tree_clo,two_clo)

#깊이 우선탐색에서 visited가 2차원 배열일 경우
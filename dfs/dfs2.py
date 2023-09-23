import sys
import math
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(node):
    visited[node]=True

    for next in range(1,n+1):
        if not visited[next] and gragh[node][next]:
            dfs(next)


n=int(input())
e=int(input())

visited=[False for _ in range(n+1)]
gragh=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(e):
    temp1,temp2=map(int,input().split())
    gragh[temp1][temp2]=gragh[temp2][temp1]=1

dfs(1)

count=visited.count(True)
print(count-1)

#깊이 우선탐색으로 몇개의 궤가 있는지 파악
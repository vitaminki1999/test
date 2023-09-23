import sys
import math
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(num):
    tree[num]=-2
    for i in range(n):
        if tree[i]==num:
            dfs(i)

n=int(input())
tree=list(map(int,input().split()))
Del=int(input())

dfs(Del)
count=0

for i in range(n):
    if tree[i]!=-2 and i not in tree:
        count+=1

print(count)

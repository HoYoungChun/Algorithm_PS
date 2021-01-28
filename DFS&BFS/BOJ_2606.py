from collections import deque

count = 0 #방문된 노드를 count

def dfs(graph,V,visited):
  global count
  visited[V]=True
  count+=1
  for i in graph[V]:
    if not visited[i]:
      dfs(graph,i,visited)

def bfs(graph,start,visited):
  global count
  queue=deque([start])
  visited[start]=True
  while queue:
    v = queue.popleft()
    visited[v]=True
    count+=1
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True


com = int(input())
net = int(input())

#방문여부 확인하는 리스트 초기화
visited=[False]*(com+1)
#인접리스트 초기화
graph = [[] for _ in range(com+1)]

for i in range(net):
  c1,c2=map(int,input().split())
  graph[c1].append(c2)
  graph[c2].append(c1)

#dfs(graph,1,visited)
bfs(graph,1,visited)

print(count-1) #1번 컴퓨터는 제외

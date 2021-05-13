#최단거리, 가중치 모두 1 -> BFS
from collections import deque

def BFS(graph, que, visited):
  while que:
    v,now_distance = que.popleft()

    if now_distance == target_distance:
      ans_city.append(v)
    
    for j in graph[v]:
      if not visited[j]:
        que.append([j,now_distance+1])
        visited[j]=True


vertex_num, edge_num, target_distance, start_vertex = map(int,input().split())

graph = [[] for _ in range(vertex_num+1)]
visited = [False]*(vertex_num+1)
ans_city =[]

for _ in range(edge_num):
  from_v,to_v = map(int,input().split())
  graph[from_v].append(to_v)

#BFS로 최단경로 구하기
que = deque()
que.append([start_vertex,0])
visited[start_vertex]= True

BFS(graph, que, visited)

#print(ans_city)

if(ans_city==[]):
  print(-1)
else:
  ans_city.sort()
  for city in ans_city:
    print(city)


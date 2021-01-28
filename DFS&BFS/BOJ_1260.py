from collections import deque

def dfs(graph,V,visited):
  visited[V]=True #방문처리
  print(V, end=' ')
  for i in graph[V]:
    if not visited[i]: #인접한 노드중 방문안된 노드
      dfs(graph,i,visited) #재귀로 시작노드 바꿔서 호출

def bfs(graph,start,visited):
  queue = deque([start]) #큐에 시작노드 추가
  visited[start]=True #방문처리
  while queue:
    v = queue.popleft() #큐에서 하나 뽑기
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i) #방문 안된 인접한 노드 모두 큐에 추가
        visited[i]=True #방문처리(다른경우에서 또 큐에 추가 안하기 위해)


N,M,V = map(int,input().split())

#방문여부 확인하는 리스트 초기화
visited=[False]*(N+1)
#인접리스트 초기화
graph = [[] for _ in range(N+1)]

#인접리스트로 그래프 저장
#번호낮은순으로 처리하도록 정렬
for i in range(M):
  v1,v2 = map(int,input().split())
  graph[v1].append(v2)
  graph[v1].sort()
  graph[v2].append(v1)
  graph[v2].sort()

dfs(graph,V,visited)
print()

#모든 노드 방문안됐음으로 초기화
visited=[False]*(N+1)
bfs(graph,V,visited)
print()

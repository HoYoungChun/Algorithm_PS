from collections import deque #bfs에서 큐 쓰기위해

'''dfs'''
def dfs(now_v):
  visited[now_v]=True #★방문처리 여기서
  print(now_v, end=' ')
  for new_v in maps[now_v]: #인접한 vertex가
    if not visited[new_v]: #방문안했으면
      dfs(new_v) #재귀호출

'''bfs'''
def bfs(q):
  while q: #큐 비면 경로있는애들은 다 방문한거다
    now_v=q.popleft() #큐에서 하나 뽑기
    print(now_v, end=' ')
    for new_v in maps[now_v]: #인접한 vertex가
      if not visited[new_v]: #방문안했으면
        visited[new_v]=True #★방문처리 여기서
        q.append(new_v) #재귀가 아닌 한번에 큐에 넣어주기


N,M,V=map(int,input().split())
vertex_num=N
edge_num=M
start_vertex=V

#인접리스트로 표현된 그래프 저장할 리스트
maps=[[]for _ in range(vertex_num+1)]
#방문여부 저장할 리스트
visited=[False]*(vertex_num+1)

#인접리스트로 그래프 저장완료
for _ in range(M):
  v1,v2=map(int,input().split())
  maps[v1].append(v2)
  maps[v2].append(v1)
  maps[v1].sort()
  maps[v2].sort() #번호 작은 vertex부터 방문하기 위해 sort

'''dfs'''
dfs(start_vertex) #시작 vertex 인자로 전달


visited=[False]*(vertex_num+1) #방문여부 초기화
print() #개행


'''bfs'''
visited[start_vertex]=True # 시작 vertex 방문처리
q=deque([start_vertex]) #큐에 시작 vertex넣어주기
bfs(q)

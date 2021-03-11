from collections import deque #bfs에서 큐 쓰기위해
import sys
sys.setrecursionlimit(10**6) #dfs에서 재귀깊이 늘리기
input=sys.stdin.readline #시간초과 방지

def bfs(q):
  while q: #경로있는 애들 다 살펴볼때까지 돈다
    now_v=q.popleft() #큐에서 뽑은 거의 현재vertex
    for new_v in maps[now_v]: #인접한 vertex들
      if not visited[new_v]: #방문 안했으면
        visited[new_v]=True #방문처리
        q.append(new_v) #큐에 넣기

def dfs(now_v):
  visited[now_v]=True
  for new_v in maps[now_v]: #인접한 vertex들
      if not visited[new_v]: #방문 안했으면
        dfs(new_v)


vertex_num,edge_num=map(int,input().split())

maps=[[] for _ in range(vertex_num+1)] #adjacency list로 그래프 저장
visited=[False]*(vertex_num+1) #방문여부 저장

for _ in range(edge_num):
  v1,v2=map(int,input().split())
  maps[v1].append(v2)
  maps[v2].append(v1) #인접 리스트로 그래프 저장

c_comp_num = 0 #연결 요소의 개수 저장할 변수
for now_v in range(1,vertex_num+1): #vertex 순서대로 보면서
  if not visited[now_v]: #방문안한 vertex일때
    c_comp_num+=1 #연결 요소의 개수 1증가
    #visited[now_v]=True #방문처리
    #q=deque([now_v])
    #bfs(q) #★경로있는 vertex들 모두 방문처리
    dfs(now_v)

print(c_comp_num)


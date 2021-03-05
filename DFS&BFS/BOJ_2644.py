from collections import deque #큐 사용하기 위해

def bfs(q):
  while q:
    v=q.popleft()
    now_v=v[0] #현재의 vertex
    count=v[1] #현재의 vertex까지의 최소 이동횟수

    if now_v==find_y: #도달했을 때(bfs니까 이때의 count가 최소)
      return count

    for adjacent_v in adjacent_list[now_v]:
      if not visited[adjacent_v]: #최단경로 찾을 때 bfs니까 방문했던데는 다시 방문필요X
        visited[adjacent_v]=True #방문처리
        q.append([adjacent_v,count+1]) #이동횟수 1증가시켜서 큐에 넣기
  
  return -1 #큐가 비워질때까지 못찾은거면 경로 없는거다


n=int(input()) #총 사람수
adjacent_list=[[] for _ in range(n+1)] #인접리스트
visited=[False]*(n+1) #index 1부터 사용하니까 (n+1)개 초기화

find_x,find_y=map(int,input().split())
m=int(input())

for _ in range(m):
  x,y=map(int,input().split())
  adjacent_list[x].append(y)
  adjacent_list[y].append(x)
#인접리스트로 그래프 저장

q=deque([[find_x,0]])
print(bfs(q))

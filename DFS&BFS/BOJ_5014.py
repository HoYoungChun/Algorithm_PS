from collections import deque

def bfs(q):
  while q:
    v=q.popleft()
    now_floor=v[0] #큐에서 뽑은 현재 층
    now_count=v[1] #현재 층까지의 이동횟수

    if now_floor==find_floor: #가려는 층에 도달했을 때
      return now_count #bfs니까 도달했을 때가 이동횟수 최소
    
    #위로 올라간 층이 범위안에 있고 방문한 적 없을 때
    if now_floor+U<=F and not visited[now_floor+U]:
      visited[now_floor+U]=True #방문처리
      q.append([now_floor+U,now_count+1]) #이동횟수 1증가시켜서 큐에 넣기

    #아래로 내려간 층이 범위안에 있고 방문한 적 없을 때
    if now_floor-D>=1 and not visited[now_floor-D]:
      visited[now_floor-D]=True
      q.append([now_floor-D,now_count+1])
  
  return "use the stairs" #큐 모두 돌아도 목표 층 도달 못하면 불가능한 경우

    
F,S,G,U,D=map(int,input().split())
start_floor=S
find_floor=G

visited=[False]*(F+1) #모든 층수에 대해

q=deque([[start_floor,0]]) #[현재 층, 현재 층까지의 이동횟수]
print(bfs(q))

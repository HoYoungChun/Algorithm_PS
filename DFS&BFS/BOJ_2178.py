from collections import deque #큐 사용하기 위해 deque import

dx = [0,0,1,-1]
dy = [1,-1,0,0] #상하좌우 방향

#★ bfs로 최단경로 구할 수 있다
def bfs(miro,sx,sy):
  queue = deque([(sx-1,sy-1)]) #(1,1)에서 시작이니까 인덱스는 (0,0)
  while queue:
    vx,vy = queue.popleft() #큐에서 하나 뽑기
    visited[vx][vy]==True #방문처리
    for i in range(4): #상하좌우 방향
      nx = vx + dx[i]
      ny = vy + dy[i]
      if 0<=nx<N and 0<=ny<M and miro[nx][ny]==1 and not visited[nx][ny]:
        count[nx][ny] = count[vx][vy]+1 #거리 1증가
        queue.append((nx,ny))
        visited[nx][ny]=True #방문처리

N,M = map(int,input().split())

miro=[list(map(int,list(input()))) for _ in range(N)] #미로 input저장
count=[[0]*M for _ in range(N)] #최단경로 길이 저장할 리스트
count[0][0]=1
visited=[[False]*M for _ in range(N)] #방문여부 저장할 리스트

bfs(miro,1,1)
print(count[N-1][M-1])

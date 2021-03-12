from collections import deque #bfs에서 큐 쓰기위해

dx=[0,0,1,-1, 1,-1,1,-1]
dy=[1,-1,0,0, 1,-1,-1,1] #상하좌우, 대각선 for문 위해

def bfs(q):
  while q:
    now_pop=q.popleft()
    now_x=now_pop[0]
    now_y=now_pop[1] #큐에서 뽑은거의 x,y좌표

    for i in range(8):
      new_x=now_x+dx[i]
      new_y=now_y+dy[i] #상하좌우,대각선의 새로운 x,y좌표
      if (0<=new_x<h) and (0<=new_y<w): #범위안에 있고
        if (maps[new_x][new_y]==1) and (not visited[new_x][new_y]): #1이고 방문안했을때
          visited[new_x][new_y]=True #방문처리
          q.append([new_x,new_y]) #큐에 넣어서 인접한 1들 있나 살펴보기


while True:
  w,h=map(int,input().split())
  if w==0 and h==0: #0 0 입력되면 break
    break
  
  maps=[list(map(int,input().split())) for _ in range(h)] #지도입력받기
  visited=[[False]*w for _ in range(h)] #방문여부 저장

  island_count=0 #섬의 개수 저장할 변수
  for i in range(h):
    for j in range(w):
      if maps[i][j]==1 and not visited[i][j]: #1이고 방문안했을때
        island_count+=1 #섬의 개수 1증가
        visited[i][j]=True #방문처리
        q=deque([[i,j]]) #큐에 x,y좌표 넣기
        bfs(q) #경로있는애들 다 visited=True로
  
  print(island_count)

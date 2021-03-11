from collections import deque #큐 쓰기위해
import sys
sys.setrecursionlimit(10**6) #dfs에서의 재귀 깊이 늘리기위해

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 for문 위해

def bfs(q):
  while q:
    now_pop=q.popleft()
    now_x=now_pop[0]
    now_y=now_pop[1] #큐에서 뽑은거의 x,y좌표
    
    for i in range(4):
      new_x=now_x+dx[i]
      new_y=now_y+dy[i]
      if (0<=new_x<M) and (0<=new_y<N): #범위안에 있고
        if (maps[new_x][new_y]==1) and (not visited[new_x][new_y]): #1이고 방문X일때
          visited[new_x][new_y]=True #방문처리
          q.append([new_x,new_y]) #큐에 넣기

def dfs(now_x,now_y):
  visited[now_x][now_y]=True
  for i in range(4):
      new_x=now_x+dx[i]
      new_y=now_y+dy[i]
      if (0<=new_x<M) and (0<=new_y<N): #범위안에 있고
        if (maps[new_x][new_y]==1) and (not visited[new_x][new_y]): #1이고 방문X일때
          dfs(new_x,new_y)


T=int(input()) #테스트케이스
for _ in range(T):
  M,N,K=map(int,input().split())
  maps=[[0]*N for _ in range(M)] #배추밭
  visited= [[False]*N for _ in range(M)] #방문여부

  for _ in range(K):
    x,y=map(int,input().split())
    maps[x][y]=1 #배추있는 곳 1로
  
  jirung_count=0 #필요한 지렁이수 저장할 변수

  for i in range(M):
    for j in range(N):
      if maps[i][j]==1 and not visited[i][j]: #배추있고 방문안한곳일때
        jirung_count+=1 #필요한 지렁이수 1증가
        #visited[i][j]=True
        #q=deque([[i,j]])
        #bfs(q) #★경로있는 1들 모두 방문처리
        dfs(i,j)
  
  print(jirung_count)

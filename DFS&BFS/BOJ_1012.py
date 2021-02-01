import sys
sys.setrecursionlimit(10**9) #★재귀깊이 연장

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 방향 설정

#★ immutable object는 call by value이고 mutable object는 call by reference로
def dfs(i,j,area,visited):
  visited[i][j]=True #방문처리
  for k in range(4): #상하좌우 방향에 대해 for문
    x = i+dx[k]
    y = j+dy[k]
    if 0<=x<M and 0<=y<N and area[x][y]==1 and visited[x][y]==False:
      dfs(x,y,area,visited) #범위안에 있고, 배추있고, 방문 안했으면 재귀호출


T=int(input()) #테스트 케이스
for _ in range(T):
  worm = 0 #필요한 지렁이 수
  M,N,K = map(int,input().split())

  #배추 심어진 위치 저장하는 Adjacent Matrix
  area = [[0]*N for _ in range(M)]

  #Adjacent Matrix에서 방문여부 Check용
  visited = [[False]*N for _ in range(M)]

  #input으로 주어지는 배추 위치 저장
  for _ in range(K):
    i,j = map(int,input().split())
    area[i][j]=1
  
  for i in range(M):
    for j in range(N):
      if area[i][j]==1 and visited[i][j]==False:
        worm+=1
        dfs(i,j,area,visited) #여기서 인접한 배추들은 모두 방문처리
  print(worm)

  

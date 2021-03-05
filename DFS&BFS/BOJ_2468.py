from collections import deque #큐 사용하기 위해

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우

def bfs(q): #bfs로 경로있는 vertex들 모두 방문처리
  while q:
    v=q.popleft()
    now_x=v[0]
    now_y=v[1] #큐에서 뽑은 vertex의 x,y좌표

    for k in range(4): #상하좌우방향
      new_x=now_x+dx[k]
      new_y=now_y+dy[k]

      if (0<=new_x<N) and (0<=new_y<N): #범위 벗어나지 않고
        if areas[new_x][new_y]>water_height and not visited[new_x][new_y]: #안전영역이면서 방문 안한 경우
          visited[new_x][new_y]=True #방문처리
          q.append([new_x,new_y]) #다음 인접한 vertex들을 살피기 위해 큐에 넣기


N=int(input())
areas=[list(map(int,input().split())) for _ in range(N)] #N*N 2차원 리스트 입력받기
max_num=-1 #답인 최대 개수 저장시킬 변수

for water_height in range(0,101): #몇층까지 잠기는지 0~100 순서대로
  count=0 #이 때의 안전영역 수 저장시킬 변수
  visited=[[False]*N for _ in range(N)] #이때의 방문여부 확인하기 위한 리스트

  for i in range(0,N):
    for j in range(0,N): #모든 지역에 대해
      if areas[i][j]>water_height and not visited[i][j]: #안전영역이면서 방문 안한 경우(새로운 구분되는 곳)
        count+=1
        visited[i][j]=True 
        q=deque([[i,j]]) #방문처리해주고 큐에 넣기
        bfs(q) #경로있는 vertex들 모두 방문처리해준다

  if count > max_num:
    max_num=count

print(max_num)

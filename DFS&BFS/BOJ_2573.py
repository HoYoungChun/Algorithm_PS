from collections import deque #큐 쓰기위해
import copy #리스트 깊은복사 하기위해
import sys #sys.stdin.readline()위해

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 방향

def bfs(q):
  global visited
  temp_q = copy.deepcopy(ices) #깊은복사

  while q:
    v=q.popleft()
    now_x=v[0]
    now_y=v[1] #큐에서 뽑은 vertex의 현재좌표

    for i in range(4):
      new_x=now_x+dx[i]
      new_y=now_y+dy[i]

      if (0<=new_x<N) and (0<=new_y<M): #범위안에 존재할 때
        if ices[new_x][new_y]==0: #바다일때
          temp_q[now_x][now_y]-=1

        #바다가 아닌 빙산이고 방문한 적 없을 때
        elif ices[new_x][new_y] !=0 and not visited[new_x][new_y]:
          visited[new_x][new_y]=True #방문처리
          q.append([new_x,new_y]) #다른 인접한 빙산 탐색위해 큐에 삽입
    
    if temp_q[now_x][now_y]<0: #음수일 경우 0으로 바꿔주기
      temp_q[now_x][now_y]=0
  
  return temp_q #새로 갱신된 빙산분포 return


N,M=map(int,sys.stdin.readline().split())
ices=[list(map(int,sys.stdin.readline().split())) for _ in range(N) ] #빙산분포 2차원 리스트
ans_year=0 #몇년경과해야 두 덩어리 이상이 되는지 저장할 변수

while True:
  block_count=0 # 이번년도 빙산분포는 몇 덩어리인지 저장할 변수

  visited=[[False]*M for _ in range(N)] #이번년도에 빙산들 방문여부

  for i in range(N):
    for j in range(M):
      if ices[i][j]!=0 and not visited[i][j]:
        block_count+=1 #한 덩어리 추가
        q=deque([[i,j]])
        visited[i][j]=True
        ices=bfs(q) #여기서 경로있는 vertex들은 모두 방문처리

  if block_count >=2: #두 덩어리 이상
    print(ans_year)
    break
  
  if block_count==0: #한 덩어리도 없음(=다 녹음)
    print(0)
    break
  
  ans_year+=1 #1년경과
  

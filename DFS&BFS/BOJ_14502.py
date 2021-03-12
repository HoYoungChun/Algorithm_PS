import copy,sys,itertools
from collections import deque #큐 쓰기위해
input=sys.stdin.readline #시간초과 방지

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 for문 위해

def bfs(q):
  while q: #경로있는애들 다 방문할 때까지 돈다
    now_pop=q.popleft()
    now_x=now_pop[0]
    now_y=now_pop[1] #현재 큐에서 뽑은거의 x,y좌표

    for i in range(4):
      new_x=now_x+dx[i]
      new_y=now_y+dy[i] #상하좌우방향의 새로운 x,y좌표
      if (0<=new_x<N) and (0<=new_y<M): #범위안에있고
        if new_map[new_x][new_y]==0 and not visited[new_x][new_y]: #0이면서 방문안했을때
          visited[new_x][new_y]=True #방문처리
          new_map[new_x][new_y]=2 #바이러스 감염되었으므로 2로 변경
          q.append([new_x, new_y]) #큐에 넣어서 새로운 x,y좌표에 인접한 0들 2로 바꿔주기


N,M=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(N)] #연구소 지도 입력받기
L=[[i for i in range(N)], [j for j in range(M)]] #combination(조합)위해 만듦


max_count=0 #안전영역의 최대 크기 저장할 변수
#★itertools.combination써서 서로 다른 세 좌표 선택
for (x1,y1),(x2,y2),(x3,y3) in list(itertools.combinations(list(itertools.product(*L)),3)):
  if maps[x1][y1]==0 and maps[x2][y2]==0 and maps[x3][y3]==0: #모두 0이면
    new_map=copy.deepcopy(maps) #연구소 지도 복사
    visited=[[False]*M for _ in range(N)] #방문여부 저장
    new_map[x1][y1]=1
    new_map[x2][y2]=1
    new_map[x3][y3]=1 #벽세우기

    #바이러스 퍼질수있는부분에 모두 퍼뜨리기
    for i in range(N):
      for j in range(M):
        if new_map[i][j]==2:
          visited[i][j]=True
          q=deque([[i,j]])
          bfs(q)

    #0의 개수 세서 최댓값이랑 비교 후 교체
    now_count=0
    for i in range(N):
      for j in range(M):
        if new_map[i][j]==0:
          now_count+=1

    if max_count<now_count:
      max_count=now_count


print(max_count) #안전영역 최대 크기 출력
              

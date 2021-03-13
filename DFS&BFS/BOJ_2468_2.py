import sys
sys.setrecursionlimit(10**6) #dfs에서 재귀깊이 늘리기
input=sys.stdin.readline #시간초과 방지
from collections import deque #bfs에서 큐 쓰기위해

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 for문 위해

def dfs(now_x,now_y):
  visited[now_x][now_y]=True #방문처리

  for i in range(4):
      new_x,new_y=now_x+dx[i],now_y+dy[i] #상하좌우 방향의 새로운 x,y좌표
      if (0<=new_x<N) and (0<=new_y<N): #범위안에 있고
        if maps[new_x][new_y]>rain_h and not visited[new_x][new_y]: #잠기지않고 방문한 적 없을때
          dfs(new_x,new_y)

def bfs(q):
  while q: #경로있는애들 다 방문할때까지
    now_x,now_y=q.popleft() #큐에서뽑은거의 x,y좌표

    for i in range(4):
      new_x,new_y=now_x+dx[i],now_y+dy[i] #상하좌우 방향의 새로운 x,y좌표
      if (0<=new_x<N) and (0<=new_y<N): #범위안에 있고
        if maps[new_x][new_y]>rain_h and not visited[new_x][new_y]: #잠기지않고 방문한 적 없을때
          visited[new_x][new_y]=True #방문처리
          q.append([new_x,new_y]) #큐에 넣어서 인접한 곳 살피기


N=int(input()) #가로 세로 크기 
maps=[list(map(int,input().split())) for _ in range(N)] #높이 정보

max_count=-1 #안전영역 최대개수

for rain_h in range(0,100): #비의 높이
  now_count=0 #안전영역 개수 세는 변수
  visited = [[False]*N for _ in range(N)] #방문여부
  for i in range(N):
    for j in range(N):
      if maps[i][j]>rain_h and not visited[i][j]: #잠기지않고 방문한적없을때
        now_count+=1 #안전영역 1증가
        #visited[i][j]=True #방문처리
        #q=deque([[i,j]]) #큐에 넣기 [x좌표,y좌표]
        #bfs(q) #bfs로 인접한 안전영역 방문처리
        dfs(i,j)
  
  max_count=max(max_count,now_count) #안전영역 최대개수 갱신

print(max_count)

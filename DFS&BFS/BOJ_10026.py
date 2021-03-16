#★파이썬에서 인자 받을때 mutual type이면 직접변경가능

from collections import deque #bfs에서 큐 사용하기 위해

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 for문 위해

#(큐,현재같은색,현재그림,현재방문여부)을 인자로
def bfs(q,now_color_num,now_map,now_visited):
  while q: #경로있는애들 다 방문할때까지 반복
    now_x,now_y=q.popleft() #큐에서 나온거의 x,y좌표

    for i in range(4): #상하좌우
      new_x,new_y=now_x+dx[i],now_y+dy[i] #새로운 x,y좌표
      if (0<=new_x<N) and (0<=new_y<N): #범위안에 있고
        if (now_map[new_x][new_y]==now_color_num) and (not now_visited[new_x][new_y]): #색이 같으면서 방문한적 없을때
          now_visited[new_x][new_y]=True #방문처리
          q.append([new_x,new_y]) #큐에 넣어서 또 인접한 애들 살피기


N=int(input()) #가로 세로 길이
maps=[list(input()) for _ in range(N)] #'R','G','B'로 입력받은 그림

dist=[[0]*N for _ in range(N)] #B:0 R:1 G:2로 변환해서 저장
dist_visited=[[False]*N for _ in range(N)] #색 구분될때의 방문여부
not_dist=[[0]*N for _ in range(N)] #B:0 R,G:1로 변환해서 저장
not_dist_visited=[[False]*N for _ in range(N)]#색 구분안될때의 방문여부

#'R','G','B'를 숫자로 변환해서 저장(하나는 R,G 다른 숫자로, 하나는 같은 숫자로)
for i in range(N):
  for j in range(N):
    if maps[i][j]=='B':
      dist[i][j]= 0
      not_dist[i][j]= 0
    elif maps[i][j]=='R':
      dist[i][j]= 1
      not_dist[i][j]= 1
    else:
      dist[i][j]= 2
      not_dist[i][j]= 1

dist_area_num=0 #R,G 구분될때 구역의 수
not_dist_area_num=0 #R,G 구분 안될때 구역의 수

for i in range(N):
  for j in range(N):
    if not dist_visited[i][j]: #R,G 구분될때 방문안한곳
      dist_visited[i][j]=True #방문처리
      dist_area_num+=1 #구역1증가
      q=deque([[i,j]]) #시작 vertex 큐에 넣기
      bfs(q,dist[i][j],dist,dist_visited) #인접한 vertex들 방문처리
    if not not_dist_visited[i][j]: #R,G 구분안될때 방문안한곳
      not_dist_visited[i][j]=True #방문처리
      not_dist_area_num+=1 #구역 1증가
      q=deque([[i,j]]) #시작 vertex 큐에 넣기
      bfs(q,not_dist[i][j],not_dist,not_dist_visited) #인접한 vertex들 방문처리

print(dist_area_num,not_dist_area_num) #R,G 구분될때와 안될때의 구역수

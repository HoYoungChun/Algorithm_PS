from collections import deque #bfs에서 큐 쓰기위해
import sys
sys.setrecursionlimit(10**6)

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 for문위해

def dfs(now_x, now_y):
  global now_count
  now_count+=1 #영역넓이 1증가

  for i in range(4):#상하좌우
      new_x,new_y=now_x+dx[i],now_y+dy[i] #새로운 x,y좌표
      if (0<=new_x<M) and (0<=new_y<N): #범위안에 있고 
        if maps[new_x][new_y]==0 and not visited[new_x][new_y]: #0이면서 방문X일때
          visited[new_x][new_y]=True #방문처리
          dfs(new_x,new_y)

def bfs(q,now_count):
  while q: #경로있는 vertex 다 방문할때까지
    now_x,now_y=q.popleft() #큐에서 나온거의 x,y좌표
    now_count+=1 #영역넓이 1증가

    for i in range(4):#상하좌우
      new_x,new_y=now_x+dx[i],now_y+dy[i] #새로운 x,y좌표
      if (0<=new_x<M) and (0<=new_y<N): #범위안에 있고 
        if maps[new_x][new_y]==0 and not visited[new_x][new_y]: #0이면서 방문X일때
          visited[new_x][new_y]=True #방문처리
          q.append([new_x,new_y]) #큐에 넣기

  return now_count #영역넓이 return


M,N,K=map(int,input().split()) #가로,세로,사각형수 입력받기
maps=[[0]*N for _ in range(M)] #모눈종이(아무것도 안그려진걸 0으로)
visited=[[False]*N for _ in range(M)] #방문여부 저장

for _ in range(K):
  y1,x1,y2,x2=map(int,input().split())
  for x in range(x1,x2):
    for y in range(y1,y2):
      maps[x][y]=1 #사각형에 해당하는 모눈종이 1로 채우기

# for m in maps:
#   print(m)

area_num = 0 #나눠지는 영역개수
area_countings=[] #영역넓이 저장할 리스트

for i in range(M):
  for j in range(N): #모눈종이 쭉 보면서
    if maps[i][j]==0 and not visited[i][j]: #0이면서 방문한적 없을때
      area_num+=1 #나눠지는 영역개수 1증가

      now_count=0 #영역의 넓이 저장할 변수
      visited[i][j]=True #방문처리
      #q=deque([[i,j]]) #시작 vertex 큐에 넣기
      #area_countings.append(bfs(q,now_count)) #인접한애들 방문처리, 개수 return
      dfs(i,j)
      area_countings.append(now_count)

print(area_num) #나눠지는 영역개수 출력
for a in sorted(area_countings): #각 영역의 넓이 오름차순 정렬
  print(a, end=' ')

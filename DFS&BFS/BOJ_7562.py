from collections import deque #큐 사용하기 위해

dx=[2,2,-2,-2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2] #나이트가 갈 수 있는 8방향

def bfs(q):
  while q:
    v=q.popleft()
    nowX=v[0]
    nowY=v[1]
    count=v[2] #이곳까지의 이동횟수

    if(nowX==target_x) and (nowY==target_y): #목표지점 도달했을 때
      return count

    for i in range(8): #나이트가 이동할 수 있는 방향
      newX=nowX+dx[i]
      newY=nowY+dy[i]

      #범위 안에 있고 방문한 적 없을 때
      if (0<=newX<I) and (0<=newY<I) and (not visited[newX][newY]):
        visited[newX][newY]=True #방문처리
        q.append([newX,newY,count+1]) #이동횟수 1증가시켜서 큐에 넣기


T = int(input()) #테스트 케이스

for _ in range(T):
  I=int(input())
  visited=[[False]*I for _ in range(I)]
  #방문여부(★bfs니까 최소경로 구할때 방문한 곳이면 다시 방문할 필요 없다)

  start_x,start_y=map(int,input().split())
  target_x,target_y=map(int,input().split())

  q=deque([[start_x,start_y,0]])#[x좌표,y좌표,이곳까지의 이동횟수]]
  visited[start_x][start_y]=True #시작점 방문처리

  print(bfs(q))

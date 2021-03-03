from collections import deque #큐 사용하기 위해
import sys #input 빠르게 하기 위해

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 방향

def bfs(q):
 while q:
   v = q.popleft()
   nowX = v[0]
   nowY = v[1]
   count = v[2] #이 위치까지의 지난횟수
   wall_break=v[3] #이 위치까지 벽 부순적 있는지

   if nowX==N-1 and nowY==M-1: #목표지점 도착했을 때 (bfs니까 찾았을때가 무조건 최소)
    return count

   for i in range(4): #큐에서 꺼낸거 기준으로 상하좌우방향
     newX=nowX+dx[i]
     newY=nowY+dy[i]

     if(0<=newX<N) and (0<=newY<M): #영역 벗어나지 않을 때

      if(maps[newX][newY]==1): # 벽이면

        if (wall_break==False) and (visited[newX][newY][1]==False): #벽 부순적 없고 방문 안했을 때(부술예정)
          visited[newX][newY][1]==True
          q.append([newX,newY,count+1,True])

      elif(maps[newX][newY]==0): #빈 공간이면

        if (wall_break==False) and (visited[newX][newY][0]==False): #벽 부순적 없고 방문 안했을 때
          visited[newX][newY][0]=True
          visited[newX][newY][1]=True #★미래에 부수면 부순 경로이므로
          q.append([newX,newY,count+1,False])

        elif (wall_break==True) and (visited[newX][newY][1]==False): #벽 부순적 있고 방문 안했을 때
          visited[newX][newY][1]=True
          q.append([newX,newY,count+1,True])

 return -1 #큐를 다 돌면서 도달하지 못했으면 도달불가능한거다


N,M = map(int,sys.stdin.readline().split())
maps = [list(map(int,sys.stdin.readline().strip()))for _ in range(N)]

visited=[[[False,False] for _ in range(M)]for _ in range(N)]
#★벽을 부순적 있는지 없는지에 따라 방문여부 따로 봐야 한다
#visited[x좌표][y좌표][벽부순경로인지(1이면 부순경로, 0이면 안부순경로)]

q=deque([[0,0,1,False]])
#[x좌표,y좌표,지난횟수,벽부순적있는지] ,출발지점도 센다고 했으므로 지난횟수 1로 시작

print(bfs(q))

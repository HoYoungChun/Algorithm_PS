from collections import deque #bfs에서 큐 쓰기위해

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우방향 for문위해

def bfs(q):
  while q:
    now_pop=q.popleft() #큐에서 하나 뽑기
    now_x = now_pop[0]
    now_y = now_pop[1]
    count = now_pop[2] #이곳까지의 이동횟수

    if (now_x==N-1) and (now_y==M-1): #★bfs니까 찾은순간이 최단경로
      return count

    for i in range(4): #상하좌우방향
      new_x=now_x+dx[i]
      new_y=now_y+dy[i]
      if (0<=new_x<N) and (0<=new_y<M): #미로범위안에 있고
        if maps[new_x][new_y]==1 and not visited[new_x][new_y]: # 이동할 수 있고, 방문한적 없을때
          visited[new_x][new_y]=True #방문처리
          q.append([new_x,new_y,count+1]) #이동횟수 1증가시켜서 큐에 넣기
        

'''최단거리 찾는거니까 bfs하면 된다'''
N,M=map(int,input().split()) #미로의 가로,세로 길이 입력받기

maps=[list(map(int,input()))for _ in range(N)] #미로 입력받기
visited=[[False]*M for _ in range(N)] #방문여부 저장

visited[0][0]=True #시작vertex 방문처리
q=deque([[0,0,1]]) #시작vertex 큐에 넣기([x좌표,y좌표,이곳까지 이동횟수])
print(bfs(q)) #bfs수행해서 최단경로 return된것 print

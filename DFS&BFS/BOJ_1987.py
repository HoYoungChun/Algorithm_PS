import sys
input=sys.stdin.readline #시간초과 방지

dx=[0,0,1,-1]
dy=[1,-1,0,0] #상하좌우 for문 위해

def dfs(now_x,now_y,count):
  global max_count #최대칸수
  
  max_count=max(max_count,count) #최대칸수 갱신

  for i in range(4):
    new_x=now_x+dx[i]
    new_y=now_y+dy[i] #상하좌우 새 x,y좌표
    if (0<=new_x<R) and (0<=new_y<C): #범위안에있고
      if not visited[ord(maps[new_x][new_y])-ord('A')]: #방문한적없는 알파벳일때
        visited[ord(maps[new_x][new_y])-ord('A')]=True #★방문처리
        dfs(new_x,new_y,count+1) #이동칸수 1증가시켜서 dfs수행
        visited[ord(maps[new_x][new_y])-ord('A')]=False #★★방문처리 해제


R,C=map(int,input().split()) #가로, 세로 크기
maps=[list(input()) for _ in range(R)] #보드 입력받기
visited=[False]*26 #알파벳 방문한적 있는지

visited[ord(maps[0][0])-ord('A')]=True #시작칸 알파벳 방문처리
max_count=1 #시작칸 하나로 방문한칸 최대1
dfs(0,0,1) #[x좌표, y좌표, 이동칸수]
print(max_count)

from collections import deque #큐 사용하기 위해 import

def bfs(q):
  while q: #큐가 빌때까지 반복(큐가 비었다는건 익을 수 있는애들은 다 익었다는 의미)
    v = q.popleft() #큐에서 하나 꺼내기
    nowX = v[0]
    nowY = v[1]
    count = v[2] #큐에서 꺼낸거까지의 지난 일수
    for i in range(4): #상하좌우 방향
      newX = nowX + dx[i]
      newY = nowY + dy[i]
      if (0 <= newX < N) and (0 <= newY < M):
        if tomatoes[newX][newY] == 0 and tomatoes[newX][newY] != -1:
          tomatoes[newX][newY] = 1 #익음처리
          q.append([newX, newY, count + 1]) #날짜 하나 더 지난 상태로 큐에 추가
  return count #큐에서 마지막으로 꺼내진거의 지난 일수(모든 토마토 익었으면 답)

def check(answer,tomatoes):
  for i in range(len(tomatoes)):
    for j in range(len(tomatoes[i])):
      if tomatoes[i][j] == 0: #익지 않은게 있다면
        return -1
  return answer

M,N = map(int,input().split())
tomatoes = [list(map(int,input().split()))for _ in range(N)] #2차원 리스트 입력받기

dx=[0,0,1,-1]
dy=[1,-1,0,0]
q=deque([]) #큐 초기화

for i in range(len(tomatoes)):
  for j in range(len(tomatoes[i])):
    if tomatoes[i][j] == 1:
      q.append([i,j,0]) #★bfs시작전에 익은 토마토 큐에 모두 넣어주기

answer = bfs(q)
print(check(answer,tomatoes))

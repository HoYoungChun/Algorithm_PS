dx=[0,0,-1,1]
dy=[-1,1,0,0] #★for문으로 접근하기 위해 방향을 리스트로 선언

village_num=0; #총 단지수
houses = [] #input으로 들어오는 집들 위치를 저장하는 2차원 리스트
village_house_num=[] #각 단지내 집의 수를 저장하는 리스트
count=0 #한 단지안에서 집의 수

#★DFS 구현
def village(i,j):
  global count
  visited[i][j]=1
  count+=1
  for k in range(4):
    x = i+dx[k]
    y = j+dy[k] #★for문으로 방향 받기
    if 0<=x<N and 0<=y<N and houses[x][y]==1 and visited[x][y]==0:
      visited[x][y]=1
      village(x,y) #재귀호출

N = int(input())
visited = [[0]*N for _ in range(N)] #N*N 배열을 0으로 초기화
for i in range(N):
    houses_input = [int(i) for i in list(input())]
    houses.append(houses_input)

for i in range(N):
  for j in range(N):
    if houses[i][j]==1 and visited[i][j]==0:
      village_num+=1
      count=0
      village(i,j)
      village_house_num.append(count)

print(village_num)
village_house_num.sort() #각 단지내 집의 수 오름차순 정렬
for v in village_house_num:
  print(v)

from collections import deque #큐 사용하기 위해
import sys # input().split() -> sys.stdin.realine().split()으로 해야 Python3로 통과됨

WHITE=0 #방문한적없는 vertex일 때(처음 초기화 상태)
RED=1
BLUE=-1 #이분 그래프면 같은 Level에 있는 vertex들은 RED나 BLUE 중 하나로 결정됨

def bfs(q):
  global false_flag

  while q:
    now_V=q.popleft() #큐에서 vertex 하나 뽑기
    now_color=color[now_V] #현재 vertex의 색

    for adj_v in adjacent_list[now_V]: #현재 vertex에 인접한 vertex들
      if color[adj_v] == now_color: #★같은색이면 이분 그래프 아님
        false_flag=1 #한번 이분 그래프 아니면 끝까지 아닌거다

      if color[adj_v]==WHITE: #색칠된 적 없는(=방문한적없는) vertex면
        color[adj_v]=now_color*(-1) #now_color가 RED일때 BLUE로, BLUE일때 RED로 칠함
        q.append(adj_v) #큐에 넣어서 다음 인접한 vertex들 살핌


K=int(input()) #테스트 케이스

for _ in range(K):
  V,E=map(int,sys.stdin.readline().split())
  color=[WHITE]*(V+1)
  adjacent_list = [[]for _ in range(V+1)] #index 1부터 쓰니까 V+1까지 초기화
  false_flag=0 #이분 그래프가 아닌지 확인하기 위해

  #그래프를 인접리스트로 저장
  for _ in range(E):
    v1,v2=map(int,sys.stdin.readline().split())
    adjacent_list[v1].append(v2)
    adjacent_list[v2].append(v1)

  #연결그래프가 아닐 수 있으므로 다음과 같이
  for i in range(1,V+1):
    if color[i]==WHITE: #색칠된 적 없는(=방문한적없는) vertex면
      q=deque([i])
      color[i]=RED
      bfs(q) #여기서 선택된 vertex와 경로가 있는 vertex들은 모두 색칠해줌

  #★flag안쓰고 sys.exit(0)하면 프로그램 종료되서 뒤의 테스트케이스들 실행안됨
  if false_flag==0: 
    print("YES")
  else:
    print("NO")

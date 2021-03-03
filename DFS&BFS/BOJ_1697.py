from collections import deque #큐 사용하기 위해

def bfs(q):
  while q: #K위치에 도달할 때까지 계속 반복(도달불가능한 경우 없으므로 무한반복해도 된다)
    v=q.popleft() #큐에서 하나 꺼내기
    nowX=v[0] #큐에서 꺼낸거의 현재위치
    count=v[1] #큐에서 꺼낸거까지의 걸린횟수

    if nowX==K: #K에 도달했다면 거기까지 걸린횟수출력(★bfs한거니까 최소횟수)
      return count

    if(0<=nowX-1) and visited[nowX-1]==False: #이렇게 체크안해주면 메모리초과
      visited[nowX-1]=True
      q.append([nowX-1,count+1])
    if(nowX+1<=100000) and visited[nowX+1]==False:
      visited[nowX+1]=True
      q.append([nowX+1,count+1])
    if(0<2*nowX<=100000) and visited[2*nowX]==False:
      visited[2*nowX]=True
      q.append([2*nowX,count+1])


N,K=map(int,input().split()) #N에서 K로 가야한다

visited=[False]*100001 #방문여부 확인용(중복방지위해)
visited[N]=True #출발점 방문처리

q=deque([[N,0]]) #[현재위치, 현재위치까지 걸린 횟수]를 큐에 넣기

print(bfs(q))

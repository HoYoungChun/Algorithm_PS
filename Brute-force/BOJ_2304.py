MAX_L = 1000 #기둥위치 인덱스 최댓값
MAX_H = 1000 #기둥높이 최댓값
heights=[0] * (MAX_L+1) #index를 1부터 접근하니까 크기 1크게

N=int(input())
for _ in range(N):
  L,H = map(int,input().split())
  heights[L]=H #L이 1000이면 1000인 인덱스

ans = 0 #h를 1부터 MAX_H까지 살피면서 그 h에 해당하는 창고넓이 더해가기
for h in range(1,MAX_H+1):
  first_flag =0 #높이가 h보다 높은 기둥이 처음 등장했는지
  start_l = 0 #맨왼쪽 기둥 인덱스
  end_l = 0 #맨오른쪽 기둥 인덱스

  for l in range(1,MAX_L+1):
    if heights[l] >=h:
      if first_flag==0: #처음등장
        start_l = l
        end_l = l
        first_flag=1
      else: #처음등장X
        end_l = l

  if first_flag == 1: #그 높이에 해당하는 기둥이 하나라도 있었다면
    ans+=end_l-start_l+1
    
print(ans)

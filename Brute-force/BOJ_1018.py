chess=[] #입력되는 체스판 저장할 리스트
N,M = map(int,input().split())

for i in range(N):
  c = list(input()) #★문자열에 list()씌워서 문자 분리
  chess.append(c)

minimum = (50*50/2) + 1
count = 0
for i in range(N-8+1):
  for j in range(M-8+1): #(i,j)가 시작점
    count = 0
    for ii in range(i,i+8):
      for jj in range(j,j+8):
        if (ii+jj)%2==0 and chess[ii][jj]=='W':
          count+=1
        if (ii+jj)%2!=0 and chess[ii][jj]=='B':
          count+=1
    count = min(count,8*8-count) #★다른경우는 전체에서 빼서 구한다
    if minimum > count:
      minimum = count
print(minimum)

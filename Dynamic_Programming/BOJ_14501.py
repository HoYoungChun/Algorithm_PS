N=int(input())
consults=[] #상담들 저장하는 리스트
dp=[0]*(N+1) #★dp[k]: k일까지의 최대이익

for i in range(N):
  one_consult=[i+1]+list(map(int,input().split()))
  one_consult[1]=one_consult[0]+one_consult[1]-1
  if one_consult[1]<=N:
    consults.append(one_consult)
#[시작일, 종료일, 수익]으로 리스트에 모두 넣어줌
consults.sort(key=lambda x:x[1]) #종료일 기준 오름차순 정렬

temp=0
for consult in consults:

  for j in range(temp+1,consult[1]): #dp의 중간에 비워진 부분을 채워주기 위해
    dp[j]=dp[j-1]

  dp[consult[1]]=max(dp[consult[1]], dp[consult[1]-1], dp[consult[0]-1]+consult[2])
  temp=consult[1]

if temp!=N: #N일차까지 dp가 채워지지 않고 끝났을 때
  for j in range(temp+1,N+1):
    dp[j]=dp[j-1]

print(dp[N])

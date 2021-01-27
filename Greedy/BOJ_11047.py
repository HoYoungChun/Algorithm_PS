coins=[] #동전의 종류저장
coin_num=0 #필요한 최소동전갯수

N,K=map(int,input().split())
#print(N,K)

for i in range(N):
  coin = int(input())
  coins.append(coin)

#print(coins)

while K!=0:
  pop_coin = coins.pop()
  coin_num += K//pop_coin
  K= K%pop_coin

print(coin_num)

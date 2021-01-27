N = int(input())
roads = list(map(int,input().split()))
oils = list(map(int,input().split()))
won = 0

oil = oils[0]

#도로 한개마다 계산해서 더해주기
for i in range(len(roads)):
  if oils[i] <= oil:
    oil = oils[i]
  won += oil * roads[i]
print(won)
  

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
  

  
N=int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

now_price = prices[0]
total_price = 0

for i,distance in enumerate(distances):
  total_price += distance*now_price
  if prices[i+1] < now_price:
    now_price = prices[i+1]

print(total_price)

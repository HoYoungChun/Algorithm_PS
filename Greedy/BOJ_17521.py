import sys

def buy(day):
  global now_coin, W
  now_coin += W // price_per_day[day]
  W -= price_per_day[day]*(W // price_per_day[day]) #가격*코인수 빼기

def sell(day):
  global now_coin, W
  W += price_per_day[day]*now_coin #코인판가격만큼 현금증가
  now_coin = 0 #모든 코인 팔았으니까 0된다


n, W = map(int,input().split())
now_coin = 0
price_per_day=[]

for _ in range(n):
  price_per_day.append(int(input()))
#print(price_per_day)

if n==1:
  print(W)
  sys.exit(0) #파이썬 강제종료

for day in range(n):
  if day==0:
    if price_per_day[day] < price_per_day[day+1]:
      buy(day)
    elif price_per_day[day] > price_per_day[day+1]:
      sell(day)
    #가격같으면 아무액션없이 뒤에 가격 같은애로 이동
  elif day==n-1:
    sell(day)
  else:
    if price_per_day[day] < price_per_day[day+1] and price_per_day[day-1] >= price_per_day[day]: #앞이랑 가격같고 뒤랑은 다르면 이때 처리해줘야
      buy(day)
    elif price_per_day[day] > price_per_day[day+1] and price_per_day[day-1] <= price_per_day[day]:
      sell(day)
    #뒤랑 가격같으면 아무액션없이 뒤에 가격 같은애로 이동

print(W)

N = int(input())
total_wait = 0 #각 손님마다 걸리는 시간의 총합

waits = list(map(int,input().split()))
waits.sort() #걸리는 시간 오름차순정렬
#print(waits)

now_sum = 0 #현재 손님 앞까지 더해진 시간

for wait in waits:
  now_sum+=wait
  total_wait+=now_sum

print(total_wait)

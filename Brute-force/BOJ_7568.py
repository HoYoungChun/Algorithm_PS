N = int(input())
dungchis=[]

for i in range(N):
  dungchi=tuple(map(int,input().split()))
  dungchis.append(dungchi) #튜플형태로 덩치들을 리스트에 저장

for dungchi in dungchis:
  count = 1
  for cdungchi in dungchis:
    #자기자신은 부등호에서 걸러진다
    if dungchi[0]<cdungchi[0] and dungchi[1]<cdungchi[1]:
      count+=1
  print(count, end=' ')

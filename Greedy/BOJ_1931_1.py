N=int(input())

meetings =[]

for _ in range(N):
  start, end = map(int,input().split())
  meetings.append([start, end])

#x[1]로 오름차순 정렬하고, 같으면 x[0]에 대해 오름차순 정렬
meetings.sort(key = lambda x : (x[1], x[0]))

ans = 0 #가능한 회의수
now_end = 0 #마지막으로 선택한 회의의 끝나는 시간
for now_meeting in meetings:
  if now_end<=now_meeting[0]:
    ans+=1
    now_end = now_meeting[1]

print(ans)

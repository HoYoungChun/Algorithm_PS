from itertools import combinations

N=int(input())
stats=[list(map(int, input().split())) for _ in range(N)] #능력치 입력받기
#print(stats)

people_comb = list(combinations(list(range(N)),N//2)) #한 팀의 조합
#print(people_comb)

ans = 9999999999

for team1 in people_comb:
  team1=list(team1) #팀1의 팀원들
  team2=[x for x in list(range(N)) if x not in team1] #팀2의 팀원들
  team1_score=0
  team2_score=0
  for players in list(combinations(team1,2)): #팀1의 팀원 2명
    team1_score+=stats[players[0]][players[1]]
    team1_score+=stats[players[1]][players[0]]
  for players in list(combinations(team2,2)): #팀2의 팀원 2명
    team2_score+=stats[players[0]][players[1]]
    team2_score+=stats[players[1]][players[0]]
  if ans > abs(team1_score-team2_score):
    ans = abs(team1_score-team2_score)

print(ans)


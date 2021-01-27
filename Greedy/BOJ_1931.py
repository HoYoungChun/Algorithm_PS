meets = [] #회의들 저장
meet_num = 0 #가능한 회의의 최대 개수

N = int(input())

for i in range(N):
    meet = tuple(map(int, input().split()))
    meets.append(meet) #튜플 형태로 회의 저장
    
#끝나는시간 기준으로 오름차순정렬
#★끝나는시간 같으면 시작시간 기준으로 오름차순정렬
meets = sorted(meets, key=lambda x: (x[1],x[0]))
#print(meets)

meet_num = 1 #정렬된 회의들에서 첫번째회의는 무조건 들어감
mini = meets[0][1] #첫번째회의의 끝나는시간

#마지막에 정답에 들어간 회의의 끝나는시간(mini)보다
#새로운회의의 시작시간이 크거나 같으면 정답구간으로 넣고
# mini값 갱신해준다
for i in range(1, N):
    if meets[i][0] >= mini:
        meet_num += 1
        mini = meets[i][1]
        
print(meet_num)

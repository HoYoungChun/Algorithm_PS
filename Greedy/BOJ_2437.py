N = int(input())
weights = list(map(int,input().split()))
weights.sort() #추들 무게순 정렬

cumulative_sum = 0 #추들 앞에서부터 누적합
for i in range(0,len(weights)):
  if cumulative_sum + 1 >= weights[i]:
    cumulative_sum += weights[i]
  else:
    break

print(cumulative_sum+1)

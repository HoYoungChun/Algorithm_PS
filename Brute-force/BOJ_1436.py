N = int(input())

num = 0 # 0부터 1씩 증가시켜서 666이 포함됐는지 확인할 수
count = 0 # 666이 포함되면 1씩 증가시키는 수

while True:
  if '666' in str(num): #★문자열로 바꿔서 666이 포함됐는지 확인
    count+=1
  if count==N: #666이 count된 횟수가 N과 같아질 때
    break
  num+=1
print(num)

import sys

def bracket_calculate(brackets):
  #print("현재의 brackets",brackets)
  if brackets =="()":
    #print(brackets,"계산결과",2)
    return 2
  elif brackets =="[]":
    #print(brackets,"계산결과",3)
    return 3
  elif brackets =="":
    #print(brackets,"계산결과",0)
    return 0
  elif len(brackets)<=2:
    print(0)
    sys.exit(0)

  if brackets[0]=="(":
    closed_flag = 1
    for idx,bracket in enumerate(brackets[1:]):
      if bracket =="(":
        closed_flag +=1
      elif bracket==")":
        closed_flag -=1
      
      if closed_flag==0: #이때 idx가 괄호끝나는 인덱스
        ans1 = bracket_calculate(brackets[1:idx+1]) #사이에 있는것만
        if(brackets[1:idx+1]==""):
          ans1=1
        #print(brackets[:idx+2],"계산결과",2*ans1)
        ans2 = bracket_calculate(brackets[idx+2:]) #전체다
        #print(brackets[idx+2:],"계산결과",ans2)
        return 2*ans1+ans2

    print(0)
    sys.exit(0)

  elif brackets[0]=="[":
    closed_flag = 1
    for idx,bracket in enumerate(brackets[1:]):
      if bracket =="[":
        closed_flag +=1
      elif bracket=="]":
        closed_flag -=1
      
      if closed_flag==0: #이때 idx가 괄호끝나는 인덱스
        ans1 = bracket_calculate(brackets[1:idx+1])
        if(brackets[1:idx+1]==""):
          ans1=1
        #print(brackets[:idx+2],"계산결과",3*ans1)
        ans2 = bracket_calculate(brackets[idx+2:])
        #print(brackets[idx+2:],"계산결과",ans2)
        return 3*ans1+ans2

    print(0)
    sys.exit(0)
    
  print(0)
  sys.exit(0)

brackets=input()
print(bracket_calculate(brackets))

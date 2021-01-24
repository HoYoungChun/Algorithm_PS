def solution(routes):
    answer = 1
    
    #끝나는 지점 기준 오름차순 정렬
    new_list = sorted(routes, key = lambda x: x[1])
    
    min = new_list[0][1]
    for route in new_list:
        if route[0] > min:
            answer+=1
            min = route[1]
    return answer

def solution(citations): #n편중 h번 이상 인용된 논문 
    answer = 0
    for h in range(10001):
        cnt = 0
        for i in citations:
            if i>=h:
                cnt=cnt+1
        if cnt>=h:
            answer = h
        else:
            break
    return answer
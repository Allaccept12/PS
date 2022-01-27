




"""
전체 논문 편중
h번이상 인용되면서 h편 이상 이면서 h편 이하가  h 잡히고
return h

[3, 0, 6, 1, 5]
"""
def solution(citations):
    answer = 0
    maxNum = max(citations)
    citations.sort(reverse=True)

    for i in citations:
        point = 0
        for j in citations:
            if j >= maxNum:
                point += 1
        if point >= maxNum and len(citations)-point <= maxNum:
            return i
        maxNum -= 1
    return answer


solution([5,5,5,5])
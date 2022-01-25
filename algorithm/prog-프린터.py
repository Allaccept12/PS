



import collections
"""

인쇄 순서 확인하고 인쇄하기
인쇄목록 가장앞에 있는것 꺼내고
대기목록에서 중요도가 자신보다 높은것이 있으면 뒤로보내고
아니면 출력

알고싶은 인쇄물이 몇번째로 인쇄는지
"""

def solution(priorities, location):
    wait = collections.deque(priorities)
    t = location
    answer = 0
    while True:
        maxNum = max(wait)
        if maxNum == wait[0]:
            if t == 0:
                answer += 1
                break
            else:
                wait.popleft()
                answer += 1
                t -= 1
                continue
        elif wait[0] < maxNum:
            if t == 0:
                wait.append(wait.popleft())
                t += len(wait)-1
            else:
                wait.append(wait.popleft())
                t -= 1

    return answer
"""

테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.66ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (0.08ms, 10.2MB)
테스트 8 〉	통과 (0.44ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.09ms, 10.2MB)
테스트 11 〉	통과 (0.34ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.30ms, 10.4MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.06ms, 10.2MB)
테스트 17 〉	통과 (0.56ms, 10.4MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.38ms, 10.2MB)
테스트 20 〉	통과 (0.06ms, 10.3MB)



"""




















solution([1, 1, 9, 1, 1, 1],0)
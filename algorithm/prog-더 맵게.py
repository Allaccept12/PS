import heapq
"""
가장 낮은 스코빌 지수 두개를
새로운 노드 = 가장 최소 노드 + 그다음 최소노드 *2
모든 노드들의 스코빌 지수를 k이상이 될때까지 반복
모든 음식을 k이상으로 섞어야하는 최소 횟수를 리턴
- 모든 음식의 스코빌 지수를 k이상으로 만들 수 없는 경우 -1 return
ex) [1, 2, 3, 9, 10, 12]
- 새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
  가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]
- 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
  새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
  가진 음식의 스코빌 지수 = [13, 9, 10, 12]
- 모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
"""

def solution(scoville, K):
    answer = 0
    cur = []
    heapq.heapify(scoville)
    while True:
        if len(scoville) < 1:
            return -1
        elif scoville[0] >= K and len(cur) == 0:
            return answer
        cur.append(heapq.heappop(scoville))
        if len(cur) == 2:
            heapq.heappush(scoville, cur[0] + (cur[1] * 2))
            answer += 1
            cur.clear()

print(solution([0,1,1],6))
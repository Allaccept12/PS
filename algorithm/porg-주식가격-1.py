



"""
초단위 주식 가격이 담긴 배열 = prices
가격이 떨어지지 않은 기간은 몇초?
[1,2,3,2,3]  [4,3,1,1,0]

0 : 가격이 떨어지지않음 4
1 : 가격이 떨어지지 않음 3
2 : 1초 이후 가격이 떨어짐 1
3 : 1초간 가격이 떨어지지 않음
4 : 0초간 가격이 떨어지지 않음
"""
import collections
def solution(prices):
    answer = []
    price = collections.deque(prices)

    while len(answer) < len(prices):
        size = len(price)
        rear = 0
        sec = 0
        while True:
            rear += 1
            if rear == size:
                answer.append(sec)
                price.popleft()
                break
            sec += 1
            if price[0] > price[rear]:
                answer.append(sec)
                price.popleft()
                break
    print(answer)
    return answer

solution([1,2,3,2,3,3,2,5,6,7,5,5,4,3,7,3,2,2,5,7,8,5,6,7,9,9,8,7,6,5,4,3,3,2,2,2,5,4])


import collections

"""
트럭에는 트럭이 다리 길이만큼 올라갈수 있고, 다리 무게도 고려 해야함
완전히 오르지 않은 트럭 무게는 무시

ex 트럭 두대 가 가능하고 무게 10kg 다리
무게가 7,4,5,6

시간 지난트럭 건너는트럭 대기트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]  [5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
"""
#2, 10, [7, 4, 5, 6]
def solution(bridge_length, weight, truck_weights):
    crossTruck = [0] * bridge_length
    waitTruck = collections.deque(truck_weights)

    #건너고있는 애들의 무게
    crossWeight = 0
    arrive = []
    time = 0
    while len(arrive) < len(truck_weights):
        # 다리길이에 비해 건너고있는 트럭갯수가 작고 ,
        # 총 중량이 건너고있는 트럭과 대기중(진입을 시도하는)에있는 트럭의 무게보다 크거나 같을떄 진입가능
        time += 1
        cur = crossTruck.pop(0)
        if cur != 0:
            crossWeight -= cur
            arrive.append(cur)
        if len(waitTruck) > 0:
            if weight >= (crossWeight + waitTruck[0]):

                crossWeight += waitTruck[0]
                crossTruck.append(waitTruck.popleft())
            else:
                crossTruck.append(0)
    return time

solution(100, 100, [10,10,10,10,10,10,10,10,10,10])








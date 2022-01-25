




"""
progresses = 먼저 배포 되어야 할 작업의 진도가 적힘
speeds = 개발속도 1일에 n퍼센트
배포는 하루에 한번만 하루의 끝에 이루어짐
ex) 작업 개발 속도가 하루에 4%라면 배포는 2일 뒤
99,99,99] [1,1,1] [3
"""
import collections



def test():
    prog = collections.deque([5, 5, 5])
    spd = collections.deque([21, 25, 20])
    if not prog:
        return []
    if not spd:
        return []

    ans = []
    ansCount = 0
    for _ in range(len(prog)):
        maxLength = len(prog)
        count = 0
        if not prog:
            break
        while True:
            if not prog:
                break
            if maxLength > len(prog) and prog[0] < 100:
                break
            elif prog[count] < 100:
                prog[count] += spd[count]
            elif prog[0] >= 100:
                count = 0
                prog.popleft()
                spd.popleft()
                ansCount += 1
            if count >= len(prog) - 1:
                count = 0
            else:
                count += 1

        ans.append(ansCount)
        ansCount = 0
    print(ans)









test()
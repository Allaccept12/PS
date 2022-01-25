






"""
 1. 정수 N이 주어짐
 2. A[N] 주어짐
 3. M이 주어짐
 4. M개의 수들이 주어짐
 -> 이 수들중 A안에 M이 존재하는지 알아내면 됨
"""

if __name__ == "__main__":
    n = int(input())
    temp = list(map(int,(input().split())))
    m = int(input())
    ms = list(map(int,(input().split())))

    for i in range(0,m):
       if ms[i] in temp:
           print(1)
       else:
           print(0)




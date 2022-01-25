







"""
n개의 음이 아닌 정수
이수를 적절히 더하고 빼서 target을 만드는 방법의 수
예)
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

return 5
"""
def solution(number, target):
    answer = 0
    leng = len(number)
    def dfs(index,value):
        nonlocal answer
        nonlocal target
        # print(answer, index, value ,leng)
        if index >= leng and target == value:
            answer +=1
            return
        if index >= leng:
            return
        # print("+ " + str(answer), index, value)
        dfs(index+1,value+number[index])

        dfs(index + 1, value - number[index])
    dfs(0,0)




solution([1,1,1,1,1],3)
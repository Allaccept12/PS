






# -> List[List[int]]
# [1,2,3,4] k = 2
def combine(n,k):
    result = []

    def backTrack(start, comb):
        if len(comb) == k:
            result.append(comb[:])
            return
        for i in range(start,n+1):
            comb.append(i)
            backTrack(i+1,comb)
            comb.pop()
            print(comb)

    backTrack(1,[])
    return result






print(combine(4,2))
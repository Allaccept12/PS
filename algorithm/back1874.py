





#1,2,5,3,4
#1
#4,3,6,8,7,5,2,1

if __name__ == "__main__":
    nums = int(input())
    result = []
    stack = []
    indexer = 1
    for i in range(nums):
        number = int(input())
        while indexer <= number:
            stack.append(indexer)
            indexer += 1
        if stack[-1] == number:
            stack.pop()
        else:
            break

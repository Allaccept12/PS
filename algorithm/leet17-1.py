import collections


def letterCombinations(digits):
    numbers = {
        '2' : "abc",
        '3' : "def",
        '4' : "ghi",
        '5' : "jkl",
        '6' : "mno",
        '7' : "pqrs",
        '8' : "tuv",
        '9' : "wxyz"
    }

    result = []
    q = collections.deque() # []
    q.append((0, ""))
    while q:
        i, c = q.popleft()
        if i == len(digits):
            result.append(c)
        else:
            nN = digits[i]
            chars = numbers[nN]
            for char in chars:
                q.append((i+1,c+char))
        print(q)
    print(result)

letterCombinations("3478")
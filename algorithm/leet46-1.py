import collections


def permutations(digits):
    #서로 다른 정수를 입력받아 가능한 모든 순열을 리턴
    result = []

    if len(digits) == 1:
        return [digits[:]]

    for _ in range(len(digits)):
        n = digits.pop(0)
        perms = permutations(digits)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        digits.append(n)
    print(result)
    return result

permutations([2,3,4,5,6,7])
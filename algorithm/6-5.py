import collections


def isGroupAnagram(src):
    #같은 문자지만 순서가 바뀐 문자들을 하나로 묶어 하나의 리스트에 담기
    result = collections.defaultdict(list)

    for i in src:
        result[tuple(sorted(i))].append(i)
        print(result)

    return list(result.values())


if __name__ == '__main__':
    print(isGroupAnagram(['bat' ,'ate','tas','tea', 'tan', 'nat', 'eat']))
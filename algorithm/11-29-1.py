






#j는 보석 s 는 갖있는 돌 s 에는 보석이 몇개나 있을까 대소문자를 구분
import collections


def findDiamond(d,s):
    # hash = collections.Counter(s)
    # count = 0
    # for f in d:
    #     count += hash[f]


    hash = collections.defaultdict()
    diamondCount = 0
    for key in d:
        vals = []
        hash[key] = None
        for val in s:
            if key == val:
                diamondCount +=1
                vals.append(val)
        hash[key] = vals








if __name__ == "__main__":
    diamond = "aA"
    stone = "aAAbbbb"
    print(findDiamond(diamond,stone))

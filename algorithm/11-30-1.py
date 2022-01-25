




"""중복 문자없는 가장 긴부분 문자열
 pwwkew -> wke
 abcabc -> abc
 다음 나오는 문자가 지금 현재 문자면 현재 인덱스 위치의 길이는 1
 다음 나오는 문자가 지금 현재 문자가 아니면 계속 탐색 하다가
 끝까지 가거나 현재 문자가 또 나오면 그 전 인덱스까지의 길이가 현재 인덱스의 길이
"""

if __name__ == "__main__":
    src = "auee"
    dic = dict()
    count = 0
    for _ in range(0,len(src)):
        dic[_] = 1
    for i in range(0,len(src)):
        # "pwwkew"
        #바로 다음 문자가 현재 문자라면
        temp = {}
        for j in range(i,len(src)):
            if src[j] in temp:
                dic[i] = count
                break
            elif src[j] != temp:
                temp[src[j]] = None
                count += 1
            if j == len(src)-1:
                dic[i] = count
        count = 0

    print(max(dic.values()))





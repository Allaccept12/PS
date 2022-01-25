


def isPalin(s):
    s = "".join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

def isLongestPalin(src):
    first = 0 #시작 단어
    last = len(src)-1 #끝단어
    palin = [] #펠린드롬 리스트
    index = 0 #순차적인 인덱스


    #cbbd
    #cd cb cb
    #bd
    #시작 5 길이가 10
    #처음부터 끝까지 검사
    while first < len(src):
        while True:
            #시작단어랑 끝단어를 검사
            if src[first] == src[last]:
                #시작단어와 끝단어가 맞다면, 시작단어부터 끝단어 까지의 펠린드롬 검사
                if isPalin(src[first:last+1]):
                    #펠린드롬 이라면 리스트에 시작단어부터 끝단어까지 짤라서 추가
                    palin.append(src[first:last+1])
                    break
                #펠린드롬이 아니라면 시작단어는 앞으로 끝단어는 뒤로 보냄
                first += 1
                last -= 1
            else:
                #시작단어와 끝단어가 맞지않다면 끝단어를 뒤로한칸
                last -= 1
                #끝단어의 위치 - 시작단어 위치 끝까지 펠린드롬이 안나오면 다음 단어로 이동
                if last-first == 1:
                    if isPalin(src[first:last+1]):
                        palin.append(src[first:last + 1])
                    break

        #그다음 단어의 인덱스 저장
        index += 1
        #시작단어의 위치이동
        first = index
        #끝단어의 위치 원상복귀
        last = len(src)-1
        print(palin)

    long = max(palin,key=len)
    return long

if __name__ == '__main__':
    print(isLongestPalin("c"))

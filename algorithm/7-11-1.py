







def solution(src):
    #나눗셈 하지않고 o(n)에 풀이
    #왼쪽에서 오른쪽으로 곱할 값 저장용 리스트
    out = []
    el = 1
    #처음 부터 왼쪽으로
    for i in range(0,len(src)):
        out.append(el)
        el *= src[i]
    el = 1
    #오른쪽에서 왼쪽으로 , 저장한 값을 차례대로 다시 곱함
    for i in range(len(src)-1,-1,-1):
        #저장한 값에 거꾸로 다시 곱해서 변경
        out[i] = out[i] * el
        #그 다음 값과 이전에 곱해진 값
        el *= src[i]

    return out




if __name__ == '__main__':
    print(solution([5,2,3,4]))
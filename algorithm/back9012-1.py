





"""
괄호문자열 = ( ) = ps
그중 괄호 모양이 바르게 구성된 문자열을 vps
한쌍의 괄호 vps
x 가 vps 라면 이것을 하나의 괄호에 넣은 새로운 문자 (x)도 vps
그리고 두 vps x 와 y를 접합 시킨 새로운 문자열 xy도 vps

assert (())()와 ((())) == vps
assert (()( , (())())) , (() != vps
"""



if __name__ == '__main__':
    T = int(input())
    opener = '('
    #전체 횟수로 돌리고
    while T:
        cover = list(input())
        empty = False
        stack = list()
        T -= 1
        #입력 받은 커버의 유효성검증
        for i in range(len(cover)):
            #오프너라면 스택에 쌓기
            if cover[i] == opener:
                stack.append(cover[i])
            else:
                #오프너아니고 스택에 암것도 없으면 break
                if not stack:
                    empty = True
                    break
                #오프너아니고 스택에 있으면 팝
                else:
                    stack.pop()
        if not stack and not empty :
            print('예쓰')
        else:
            print('노')











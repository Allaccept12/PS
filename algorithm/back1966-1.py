
"""
 3 테스트 수
1 0 n = 문서의 개수 , m = 궁금한 문서
5   중요도 = 5
4 2  n = 문서의 개수 , m = 궁금한 문서
1 2 3 4  중요도 = 1,2,3,4
6 0  n = 문서의 개수 , m = 궁금한 문서
1 1 9 1 1 1  중요도 = 1,1,9,1,1,1

 출력 :
1
2
5
"""
import collections

if __name__ == '__main__':
    case = int(input())
    for i in range(case):
        n,m = map(int,input().split())
        important = list(map(int, input().split()))
        important_ = [0 for s in range(n)]
        important_[m] = -1
        cont = 0
        while True:
            if max(important) == important[0]:
                cont += 1
                if important_[0] == -1:
                    print(cont)
                    break
                else:
                    del important_[0]
                    del important[0]

            else:
                important_.append(important_[0])
                important.append(important[0])
                del important[0]
                del important_[0]
            print(important, important_)





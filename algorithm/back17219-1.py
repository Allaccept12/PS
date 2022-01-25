



"""
    n = 저장된 사이트수
    m = 찾으려는 사이트 주소 수

    n + 2 줄부터 비밀번호를 찾고자하는 주소가출력
    비밀번호 차례로 출력


"""


if __name__ == "__main__":
    n,m = map(int,input().split())
    dic = {}
    for i in range(n):
        siteAdd, password = map(str, input().split())
        dic[siteAdd] = password
    for i in range(m):
        wantFindPassword = input()
        print(dic[wantFindPassword])




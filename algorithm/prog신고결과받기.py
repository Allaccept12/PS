








"""
1. 각 유저는 한번에 한명의 유저만 신고할수있음
2. 한 유저가 신고를 했던 유저를 또다시 신고 할경우 경고는 1회로  그침.
3. k번 이상 신고된 유저는 정지메일 발송
4. 정지당한 유저를 신고한 모든 유저는 정지 사실 메일 발송
5. return 은 정지메일과, 정지사실메일을 포함한 유저가 받은 메일 카운트를 리턴
"""
import collections


def solution(id_list, report, k):
    requester = collections.defaultdict(set) #행한
    responser = {} #당한
    report = set(report) #중복제거
    overLife = [] #끝난
    result = [0] * len(id_list) #add 쓰려고

    for i in id_list:
        responser[i] = 0
    for i in report:
        report,response = i.split()
        responser[response] += 1
        requester[report].add(response)
        if responser[response] == k:
            overLife.append(response)

    print(responser)
    print(requester)
    print(overLife)

    for i in overLife:
        for j in range(0,len(id_list)):
            if i in requester[id_list[j]]:
                result[j] += 1
                print(result)

    print(result)
    return result








solution(["muzi","frodo","apeach","neo"],
         ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
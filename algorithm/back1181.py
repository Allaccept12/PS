






"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
3. 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
첫째 줄에 단어의 개수 N이 주어진다.
(1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
주어지는 문자열의 길이는 50을 넘지 않는다.
"""
import sys
n = int(sys.stdin.readline())
chars = set(list(sys.stdin.readline().rstrip() for _ in range(n)))
chars = list(chars)

def merge(arr1, arr2):
    result = []
    i=j=0
    #1. 길이가 짧은 것부터
    #2. 길이가 같으면 사전 순으로
    while i < len(arr1) and j < len(arr2):
        if len(arr1[i]) == len(arr2[j]):
            if arr1[i] < arr2[j]: #arr1 이빠르다면
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        else:
            if len(arr1[i]) < len(arr2[j]):
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result



def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]

    return merge(mergeSort(L),mergeSort(R))

print(mergeSort(chars))










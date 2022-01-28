






"""
힙은 최대 최소 값을 빨리 찾기위해 고안된 완전이진트리
부모는 자식보다 커야함
1. 루트노드와 맨끝에 있는 원소를 교체한다.
2. 맨뒤에 있는 원소를 (원래 루트 노드)를 삭제한다.
3. 변경된 노드와 지삭 노드들을 비교 . 두자식 중 더 큰 자식과 빅해서 자신보다 자식이 더크다면 자리를 바꿈
4. 자식 노드 둘보다 부모노드가 크거나 가장 바닥에 도달하지 않을때까지 반복
5. 2에거 제거한 원래 루트노드를 반환
"""

import heapq



def solution(k,lst):
    print(heapq.nlargest(k,lst))




solution(3,[3, 2, 3, 1, 2, 4, 5, 5, 6])



# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
# assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1
#
#
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
# assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1
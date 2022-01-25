from collections import deque


def get_card(num):
    # 제일 위 카드버리기
    nums = deque([n for n in range(1,num+1)])

    while len(nums) > 1:
        nums.popleft()
        nums.append(nums.popleft())
    # 제일 위 카드 뒤로옮기기
    # 한장 남은 카드 반환
    return nums.pop()

if __name__ == '__main__':
    print(get_card(6))

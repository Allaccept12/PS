"""
```python
[4, 6, 2, 9, 1]  # 정렬되지 않은 배열

1단계 : [**4**, 6, 2, 9, 1]
        4는 현재 정렬되어 있는 부대원입니다.
			  그럼 이제 새로운 신병인 6을 받습니다.
        4, **6** 이 되는데 4 < 6 이므로 그대로 냅둡니다.
       [**4, 6,** 2, 9, 1] 이렇게요!

자, 그러면 이제 한 바퀴를 돌렸죠?
이 과정에서 새로운 부대원인 4, 6은 현재 정렬된 상태입니다!
이처럼, 삽입 정렬은 한 바퀴가 돌 때마다 정렬된 상태가 됩니다.
끝까지 한 번 반복해볼게요!

2단계 : [**4, 6,** 2, 9, 1]
        4, 6 은 현재 정렬되어 있는 부대원입니다.
        그럼 이제 새로운 신병인 2를 받습니다.
        4, 6, **2** 가 되는데 6 > 2 이므로 둘을 변경합니다!
        4, **2**, 6 가 되는데 4 > 2 이므로 둘을 변경합니다!
       [**2, 4, 6**, 9, 1] 이렇게요!

3단계 : [**2, 4, 6**, 9, 1]
        2, 4, 6 은 현재 정렬되어 있는 부대원입니다.
        그럼 이제 새로운 신병인 9를 받습니다.
        2, 4, 6, **9** 가 되는데 6 < 9 이므로 그대로 냅둡니다.
       [**2, 4, 6, 9**, 1] 이렇게요!

4단계 : [**2, 4, 6, 9**, 1]
        2, 4, 6, 9 은 현재 정렬되어 있는 부대원입니다.
        그럼 이제 새로운 신병인 1을 받습니다.
        2, 4, 6, 9, **1** 가 되는데 9 > 1 이므로 둘을 변경합니다!
        2, 4, 6, **1,** 9 가 되는데 6 > 1 이므로 둘을 변경합니다!
        2, 4, **1**, 6, 9 가 되는데 4 > 1 이므로 둘을 변경합니다!
        2, **1**, 4, 6, 9 가 되는데 2 > 1 이므로 둘을 변경합니다!
       **[1, 2, 4, 6, 9]** 이렇게요!

자, 모두 정렬이 되었습니다! 어떠신가요? 감이 좀 오시나요?
```
"""


def insertionsort_2(lst):
    for idx in range(1, len(lst)):
        val = lst[idx]
        cmp = idx - 1

        while lst[cmp] > val and cmp >= 0:
            lst[cmp + 1] = lst[cmp]
            cmp -= 1

        lst[cmp + 1] = val

    return lst









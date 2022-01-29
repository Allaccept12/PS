from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#[-1,5,3,4,0]
#[4,2,1,3]
#
def sortList(self, head: Optional[ListNode]):
    if head is None or head.next is None:
        return head
    temp = []
    headTemp = head
    while headTemp:
        temp.append(headTemp.val)
        headTemp = headTemp.next

    temp.sort()
    pointer = head

    for i in temp:
        head.val = i
        head = head.next
    return pointer





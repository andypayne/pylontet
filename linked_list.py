# Self is introduced in Python 3.11+, so use either annotations or typing_extensions (which may require installation).
# from __future__ import annotations
from typing_extensions import Self
from typing import Any, Optional  # , Self


class ListNode:
    # def __init__(self, data: Any = None, next: Optional[ListNode] = None):
    def __init__(self, data: Any = None, next: Optional[Self] = None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(data={self.data}, next={self.next})"


if __name__ == "__main__":

    def merge_lists(lst1, lst2):
        merged = ListNode()
        cur_node = merged
        while lst1 and lst2:
            if lst1.data < lst2.data:
                cur_node.next = lst1
                lst1 = lst1.next
            else:
                cur_node.next = lst2
                lst2 = lst2.next
            cur_node = cur_node.next
        if lst1:
            cur_node.next = lst1
        elif lst2:
            cur_node.next = lst2
        return merged.next

    list1 = ListNode(10)
    list1.next = ListNode(20)
    list1.next.next = ListNode(30)
    list2 = ListNode(15)
    list2.next = ListNode(25)
    list2.next.next = ListNode(35)
    print(f"list1:\n  {list1}")
    print(f"list2:\n  {list2}")
    merged = merge_lists(list1, list2)
    print(f"Merged:\n  {merged}")
    assert merged.data == 10
    assert merged.next.data == 15
    assert merged.next.next.data == 20
    assert merged.next.next.next.data == 25
    assert merged.next.next.next.next.data == 30
    assert merged.next.next.next.next.next.data == 35

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next

if __name__ == "__main__":
    def build_linked_list(values):
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head


    def print_linked_list(head):
        values = []  
        while head:
            values.append(str(head.val))  
            head = head.next
        print("->".join(values)) 


    ans = Solution().mergeTwoLists(
            build_linked_list([1,2,4]),
            build_linked_list([1,3,4])
        )

    print_linked_list(ans)
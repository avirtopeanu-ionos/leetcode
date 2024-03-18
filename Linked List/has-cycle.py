from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Tortoise and hare. If the hare catches up to the tortise, there's a loop.
    # Alternative: O(n) space with a set. If already seen value, return True.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while True:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        

if __name__ == "__main__":
    def build_linked_list(values):
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    list = build_linked_list([5, 4, 3, 2, 1])
    p = list
    while(p.next):
        p = p.next
    p.next = list.next


    print(Solution().hasCycle(list))
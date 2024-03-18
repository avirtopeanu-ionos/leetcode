from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            # Treat this stupid case 
            return None

        stack = [head.val] # Safe because at least 1 element
        while head.next != None:
            head = head.next
            stack.append(head.val)

        ans = ListNode(stack.pop()) # Safe because at least 1 element
        prev = ans
        while len(stack) > 0:
            pointer = ListNode(stack.pop())
            prev.next = pointer
            prev = pointer

        return ans



if __name__ == "__main__":
    def build_linked_list(values):
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    rev = Solution().reverseList(build_linked_list([5, 4, 3, 2, 1]))
    print(rev.next.val)
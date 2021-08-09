# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num_list=[] #연결리스트에서 값들만 빼서 저장할 리스트
        
        while head!=None: #다음 연결리스트가 없을때까지
            num_list.append(head.val)
            head = head.next
            
        return num_list == num_list[::-1] #뒤집어서 같은지(O(N))

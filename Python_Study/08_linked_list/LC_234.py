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

    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: Deque = collections.deque() #deque 선언
        
        if not head: #빈 연결리스트일때
            return True
        
        node = head
        while node != None:
            q.append(node.val)
            node = node.next
        
        while len(q)>1:
            if q.popleft() != q.pop():
                return False #하나라도 앞,뒤 대칭되는위치에 다른게 있으면 False
            
        return True
    
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None #역순 연결 리스트
        slow=fast=head #시작할때는 모두 head에서
        
        #런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next #두칸씩 이동
            rev,rev.next,slow = slow,rev,slow.next #한칸씩 이동
        if fast:
            slow=slow.next #입력값 홀수일때 slow 한칸 더 앞으로 이동
        
        #팰린드롬 여부 확인(slow의 나머지 이동경로와 rev 비교)
        while rev and rev.val == slow.val:
            slow,rev = slow.next,rev.next
        return not rev

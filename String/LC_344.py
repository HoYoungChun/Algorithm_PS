class Solution:
    def reverseString(self, s: List[str]) -> None:
    	s[:]=s[::-1]
        
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
          s[left], s[right] = s[right], s[left]
          left += 1
          right -= 1

        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0,len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i] #교환

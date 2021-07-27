class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ','') #모두 소문자로+공백제거
        refined_s = '' #숫자,문자만 남길 문자열
        for one_s in s:
          if one_s.isdigit() or one_s.isalpha(): #숫자거나 문자일때만
            refined_s+= one_s
        
        if refined_s == refined_s[::-1]: #뒤집어도 같다면
            return True
        else:
            return False
      
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ','') #모두 소문자로+공백제거
        refined_s = '' #숫자,문자만 남길 문자열
        for one_s in s:
          if one_s.isalnum(): #숫자거나 문자일때만
            refined_s+= one_s
        
        return refined_s == refined_s[::-1] #뒤집어도 같은지

    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #모두 소문자로
        s = re.sub('[^a-z0-9]','',s) #문자,숫자만 남기기
        return s == s[::-1]

    
class Solution:
    def isPalindrome(self, s: str) -> bool:
      strs: Deque = collections.deque()

      for char in s:
        if char.isalnum():
          strs.append(char.lower()) #소문자로 넣기

      while len(strs) > 1:
        if strs.popleft() != strs.pop(): #하나라도 다른게 있으면
            return False

      return True

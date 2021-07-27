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

class Solution:
    def reverseString(self, s: List[str]) -> None:
        #s.reverse()로 된다
        #s=s[::-1] #공간복잡도 O(1)로 제한되어있어서 안됨 s[:]=s[::-1]은 된다
        for i in range(0,len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i] #교환

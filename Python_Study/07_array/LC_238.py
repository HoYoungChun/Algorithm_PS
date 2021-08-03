class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        
        #[1,2,3,4]일때
        
        #왼쪽부터 곱셈해나가기
        #자기자신을 제외한 왼쪽의 곱셈결과 p는 [1,1,2,6]
        for i in range(0,len(nums)): #i는 0,1,2,3
            out.append(p)
            p = p * nums[i]
        
        p=1
        
        #오른쪽부터 곱셈해나가기
        #자기자신을 제외한 오른쪽의 곱셈결과 p는 [1,4,12,24]
        for i in range(len(nums)-1,0-1,-1): #i는 3,2,1,0
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out

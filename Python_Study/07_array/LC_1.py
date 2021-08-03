class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            if target - n in nums[i+1:]: #nums에서 인덱스 i 이후에 target-n 있는지 살피기
                return [nums.index(n), nums[i+1:].index(target-n) + (i+1)] #해당 index반환
              
              
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i,num in enumerate(nums):
            new_dict[num] = i #그 값에 대한 index를 value로 저장(여러개면 맨뒤에 있는걸로 저장)
            
        for i,k in enumerate(new_dict): #i는 k에 해당하는 인덱스
            if target-k in new_dict:
                if i!=new_dict[target-k]: #같은 인덱스 아니면
                    return [i,new_dict[target-k]]
                  
                  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        #하나의 for문으로 통합
        for i,num in enumerate(nums):
            if target- num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

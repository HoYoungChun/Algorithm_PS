class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.sort() #정렬
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1 #인덱스 i+1부터 끝까지
            
            while left < right: #left랑 right 만나기 전까지
                sum = nums[i] + nums[left] + nums[right]
            
                if sum < 0:
                    left+= 1
                elif sum > 0:
                    right -=1
                else: #sum이 0인 경우이므로 정답
                    results.append([nums[i] , nums[left] , nums[right]])
                    left+=1
                    right-=1
        
        #중복제거
        new_results=[]
        for res in results:
            if res not in new_results:
                new_results.append(res)
                
        return new_results
      
      
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.sort() #정렬
        
        for i in range(len(nums)-2):
            #앞이랑 같은 중복된 수 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1 #인덱스 i+1부터 끝까지
            
            while left < right: #left랑 right 만나기 전까지
                sum = nums[i] + nums[left] + nums[right]
            
                if sum < 0:
                    left+= 1
                elif sum > 0:
                    right -=1
                else: #sum이 0인 경우이므로 정답
                    results.append([nums[i] , nums[left] , nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    
                    left+=1
                    right-=1
        
        return results

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = 10**5 #가격 최소값
        result = 0 #시세차익 최대값
        
        for price in prices:
            if minimum > price:
                minimum = price #현재 price가 minimum보다 작으면 갱신
            
            if minimum < price: #현재 price가 minumum보다 크면
                result = max(result,price-minimum) #시세차익 구해서 기존보다 크면 갱신
                
        return result
      
      
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = sys.maxsize #가격 최소값
        result = 0 #시세차익 최대값
        
        for price in prices:
            minimum = min(minimum,price) #현재 price가 minimum보다 작으면 갱신
            result = max(result,price-minimum) #시세차익 구해서 기존보다 크면 갱신
                
        return result

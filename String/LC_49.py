class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict=defaultdict(list) #기본 value가 []
        for str in strs:
          key = tuple(sorted(str)) # 내부 알파벳 정렬해서 key값으로
          new_dict[key].append(str)
        return list(new_dict.values())

    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict=defaultdict(list) #기본 value가 []
        for str in strs:
          new_dict[''.join(sorted(str))].append(str)
        return list(new_dict.values())

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits=[] #digit-logs
        letters=[] #letter-logs
        
        for log in logs: #digit-log, letter-log나누기
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        #content로 1차비교, identifier로 2차비교 통해 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
                    
        return letters + digits #리스트 합치기

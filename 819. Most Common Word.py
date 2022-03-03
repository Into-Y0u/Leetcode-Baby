from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in string.punctuation: 
            paragraph = paragraph.replace(c, " ")
        temp = Counter(paragraph.lower().split())
        
        for i,n in temp.most_common():
            if i not in banned:
                return i
        return None

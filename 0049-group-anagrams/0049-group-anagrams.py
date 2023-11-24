class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = {}
        
        for word in strs:
            key = ''.join(sorted(word))
            
            if key in words:
                words[key].append(word)
            else:
                words[key] = [word]
        
        return words.values()
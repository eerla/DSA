class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1+count.get(n, 0)
            
        for val, cnt in count.items():
            freq[cnt].append(val)
            
        res = []
        # print(count, freq)
        for bkt in range(len(freq)-1, -1, -1):
            # print(bkt)
            if freq[bkt]:
                for i in freq[bkt]:
                
                    res.append(i)
                    if len(res) == k:
                        return res
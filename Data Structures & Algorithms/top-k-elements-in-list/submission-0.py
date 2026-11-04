import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencySet = {}

        for num in nums: 
            frequencySet[num] = frequencySet.get(num, 0) + 1 

        heap = [(-count, num) for num, count in frequencySet.items()]
        heapq.heapify(heap)

        returnList = [] 
        for _ in range(k):
            count, num = (heapq.heappop(heap))
            returnList.append(num) 
            
        return returnList

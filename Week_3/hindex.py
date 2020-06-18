# Approach 1 : O(n) - Not gonna work in an interview
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        answer = 0
        for i in range(N):
            if citations[i] >= N-i and answer< N-i:
                answer = N-i
        return answer
            

#Since list is sorted we should look for O(logn) solution. Something by the line of Binary Search.
# Approach 2 : O(logn)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        low, high = 0,len(citations)
        answer = 0
        while low < high:
            mid = (low + high)//2
            if citations[mid] < N - mid:
                low = mid + 1
            else:
                answer = max(answer, N - mid)
                high = mid
        return answer
            
            
                
        
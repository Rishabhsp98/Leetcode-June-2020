#Approach 1: Easiest Solution would be to use Dictionary to store frequencies of every element and returning the key having 1 as value.
#But this approach has time complexity of O(n) as well as space complexity of O(n)


#Approach 2: return (3 * sum(set(nums)) - sum(nums)) // 2. This will impress a mathematician maybe but not the recruiter.
# Time Complexity: O(n) Space Complexity: O(n)

#Approach 3: Do Quick Sort and then compare ith element with i+2th element if same i=i+3 else we have the answer.
#Time Complexity: O(nlogn) and Space Complexity: O(1)

#Approach 4: Bit Manipulation.Time Complexity: O(n) And Space Complexity: O(1) But Good luck explaining this to a recruiter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos, not_threes = 0, 0, 0
        for n in nums:
            twos |= (ones & n)
            ones ^= n
            not_threes = ~(ones & twos)
            ones &= not_threes
            twos &= not_threes
        
        return ones
        
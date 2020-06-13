class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums

        nums = sorted(nums)
        N = len(nums)

        f = [1] * N
        pi = [0] * N
        mx = 1
        mx_idx = 0

        for i in range(N):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and f[i] < f[j] + 1:
                    f[i] = f[j] + 1
                    pi[i] = j
                    if mx < f[i]:
                        mx = f[i]
                        mx_idx = i

        res = list()
        for k in range(mx):
            res.append(nums[mx_idx])
            mx_idx = pi[mx_idx]

        return res[::-1]
        
#Approach 1: BruteForce - Solves the problem - Don't use in interviews due to use of inbuilt libraries

from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        string = "123456789"[:n]
        permut = list(permutations(string))
        return(str(''.join(permut[k-1])))
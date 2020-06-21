class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[math.inf for x in range(cols+1)] for y in range(rows+1)]
        dp[rows][cols-1], dp[rows-1][cols] = 1, 1
        
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                dp[i][j] = min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j]
                
                if dp[i][j]<1:
                    dp[i][j] = 1
                    
        return dp[0][0]
        
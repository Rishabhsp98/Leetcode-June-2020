class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomList = []
        self.randomSet = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.randomSet:
            self.randomSet[val] = len(self.randomList)
            self.randomList.append(val)
            return True
        return False
            
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.randomSet:
            return False
        
        index = self.randomSet[val]
        self.randomList[index]= self.randomList[-1]
        self.randomSet[self.randomList[index]] = index
        self.randomList.pop()
        del self.randomSet[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.randomList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
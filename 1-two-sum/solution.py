class Solution(object):
    def twoSum(self, nums, target):
        
        prevMap = {} # val : index

        for i, n in enumerate(nums): # to get index and actual number
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

        

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numTracker = []

        for i in nums:
            if i in numTracker:
                return True

            numTracker.append(i)

        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        a = len(set(nums))
        b = len(nums)

        if b > a:
            return True
        else:
            return False
        
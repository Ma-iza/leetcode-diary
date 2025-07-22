from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        maxs = curr

        for i in range(k, len(nums)):
            curr = curr + nums[i] - nums[i - k]
            maxs = max(curr, maxs)

        return maxs / k

if __name__ == "__main__":
    nums_input = input("Enter the list of numbers separated by spaces: ")
    nums = list(map(int, nums_input.strip().split()))
    
    k = int(input("Enter the value of k: "))

    sol = Solution()
    result = sol.findMaxAverage(nums, k)
    print(f"The maximum average of a subarray of length {k} is: {result}")


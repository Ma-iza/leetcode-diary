from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxi = 0
        numzeroes = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                numzeroes += 1
            while numzeroes > k:
                if nums[left] == 0:
                    numzeroes -= 1
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi

# Full input/output wrapper
def main():

    nums = list(map(int, input("Enter the binary array: ").strip().split()))
    k = int(input("Enter k: ").strip())

    sol = Solution()
    result = sol.longestOnes(nums, k)
    print("Longest subarray with at most", k, "zeroes:", result)

if __name__ == "__main__":
    main()

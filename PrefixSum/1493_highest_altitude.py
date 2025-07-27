from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        altitude = 0
        for num in gain:
            altitude += num
            highest = max(highest, altitude)
        return highest

if __name__ == "__main__":
    solution = Solution()
    
    # Test case
    gain = [-5, 1, 5, 0, -7]
    result = solution.largestAltitude(gain)
    
    print("Input gain:", gain)
    print("Highest altitude:", result)

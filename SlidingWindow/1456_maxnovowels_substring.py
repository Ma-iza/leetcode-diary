class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        maxi = 0
        vowels = 'AEIOUaeiou'
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxi = count  
        for j in range(k, len(s)):
            if s[j - k] in vowels:
                count -= 1
            if s[j] in vowels:
                count += 1
            maxi = max(count, maxi)
        return maxi


def main():
   
    s = input("Enter the string: ").strip()
    k = int(input("Enter k: ").strip())

    sol = Solution()
    result = sol.maxVowels(s, k)
    print("Maximum number of vowels in any substring of length", k, ":", result)

if __name__ == "__main__":
    main()

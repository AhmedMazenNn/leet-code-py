class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)  # Convert string to list for in-place modification
        left, right = 0, len(s) - 1  # Two-pointer approach

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]  # Swap vowels
                left += 1
                right -= 1

        return "".join(s)  # Convert list back to string

# Test case:
solution = Solution()
print(solution.reverseVowels("IceCreAm"))  # Expected Output: "AceCreIm"
print(solution.reverseVowels("leetcode"))  # Expected Output: "leotcede"

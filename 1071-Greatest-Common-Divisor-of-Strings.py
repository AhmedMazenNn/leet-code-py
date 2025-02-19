from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 and str2 have a common divisor string
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of lengths
        gcd_length = gcd(len(str1), len(str2))
        
        # The greatest common divisor string
        return str1[:gcd_length]

# Test cases
sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))   # Output: "ABC"
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(sol.gcdOfStrings("LEET", "CODE"))    # Output: ""

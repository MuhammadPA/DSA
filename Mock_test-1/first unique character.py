'''First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return i
        return -1

s1 = "leetcode"
a=Solution()
result1=a.firstUniqChar(s1)
print(result1) #Output:0


s2 = "loveleetcode"
b=Solution()
result2=b.firstUniqChar(s2)
print(result2) #Output:2

s3 = "aabb"
c=Solution()
result3=c.firstUniqChar(s3)
print(result3) #Output:-1


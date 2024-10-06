"""Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300]."""

class Solution:
    def decodeString(self, s: str) -> str:
        def ans(self,s):
            if s.count('[')==0:
                return s
            for x in range(len(s)):
                if s[x]=='[':
                    i = x-1
                    k = ""
                    self.c = 0
                    while i>-1 and s[i].isdigit():
                        k += s[i]
                        i -= 1
                        self.c += 1
                    k = k[::-1]
                    k = int(k)
                    mx = x-self.c
                if s[x]==']':
                    my = x-1
                    t = ""
                    t += k*s[mx+self.c+1:my+1]
                    s = s[:mx]+t+s[my+2:]
                    return ans(self,s)
        return ans(self,s)
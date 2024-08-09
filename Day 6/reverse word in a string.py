"""Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s."""



class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        
        s=s[::-1]
        s=(" ".join(s))
        return s
    
# OR


class Solution:
    def str_rev(self, _str, start_rev, end_rev):
        while start_rev < end_rev:
            _str[start_rev], _str[end_rev] = _str[end_rev], _str[start_rev]
            start_rev += 1
            end_rev -= 1
    
    def reverseWords(self, s: str) -> str:
        s = re.sub(' +', ' ', s.strip())
        s = list(s)
        str_len = len(s) - 1
        self.str_rev(s, 0, str_len)
        start = 0

        for end in range(0, str_len + 1):
            if end == str_len or s[end] == ' ':
                end_idx = end if end == str_len else end - 1
                self.str_rev(s, start, end_idx)
                start = end + 1

        return ''.join(s)

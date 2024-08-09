"""Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.
Note : All characters are in Lowercase alphabets. 

Example 1:

Input:
S = "timetopractice"
P = "toc"
Output: 
toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.
Example 2:

Input:
S = "zoomlazapzo"
P = "oza"
Output: 
apzo
Explanation: "apzo" is the smallest 
substring in which "oza" can be found.
Your Task:
You don't need to read input or print anything. Your task is to complete the function smallestWindow() which takes two string S and P as input paramters and returns the smallest window in string S having all the characters of the string P. In case there are multiple such windows of same length, return the one with the least starting index. 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(n) n = len(p)

 

Constraints: 
1 ≤ |S|, |P| ≤ 105"""

class Solution:
    def smallestWindow(self, s, p):
        if len(s) < len(p):
            return "-1"
    
        freqP = {}
        for char in p:
            freqP[char] = freqP.get(char, 0) + 1
        
        required = len(freqP)
        formed = 0
        l, r = 0, 0
        windowCounts = {}
        ans = float("inf"), None, None
        
        while r < len(s):
            char = s[r]
            windowCounts[char] = windowCounts.get(char, 0) + 1
            
            if char in freqP and windowCounts[char] == freqP[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                windowCounts[char] -= 1
                if char in freqP and windowCounts[char] < freqP[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "-1" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

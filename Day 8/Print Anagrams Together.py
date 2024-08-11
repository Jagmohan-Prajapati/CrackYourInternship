"""Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

Note: The final output will be in lexicographic order.


Example 1:

Input:
N = 5
words[] = {act,god,cat,dog,tac}
Output:
act cat tac 
god dog
Explanation:
There are 2 groups of
anagrams "god", "dog" make group 1.
"act", "cat", "tac" make group 2.
Example 2:

Input:
N = 3
words[] = {no,on,is}
Output: 
is
no on
Explanation:
There are 2 groups of
anagrams "is" makes group 1.
"no", "on" make group 2.

Your Task:
The task is to complete the function Anagrams() that takes a list of strings as input and returns a list of groups such that each group consists of all the strings that are anagrams.


Expected Time Complexity: O(N*|S|*log|S|), where |S| is the length of the strings.
Expected Auxiliary Space: O(N*|S|), where |S| is the length of the strings.


Constraints:
1<=N<=100

1<=|S|<=10"""


from collections import defaultdict

class Solution:
    def Anagrams(self, words, n):
        anagrams_map = defaultdict(list)
    
        # Group words by sorted string as key
        for word in words:
            sorted_word = ''.join(sorted(word))
            anagrams_map[sorted_word].append(word)
        
        # Collecting results in order of appearance
        result = []
        for group in anagrams_map.values():
            result.append(' '.join(group))
        
        return result
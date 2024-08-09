"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        output = []
        backtrack(n, 0, 0, output, result)
        return result

def backtrack(n, leftCount, rightCount, output, result):
    if leftCount >= n and rightCount >= n:
        outputStr = "".join(output)
        result.append(outputStr)

    if leftCount < n:
        output.append("(")
        backtrack(n, leftCount + 1, rightCount, output, result)
        output.pop()

    if rightCount < leftCount:
        output.append(")")
        backtrack(n, leftCount, rightCount + 1, output, result)
        output.pop()
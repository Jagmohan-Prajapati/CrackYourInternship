"""Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
0 <= num <= 231 - 1"""

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        bigString = ["Thousand", "Million", "Billion"]
        result = self.numberToWordsHelper(num % 1000)
        num //= 1000
        
        for i in range(len(bigString)):
            if num > 0 and num % 1000 > 0:
                result = self.numberToWordsHelper(num % 1000) + bigString[i] + " " + result
            num //= 1000
        
        return result.strip()

    def numberToWordsHelper(self, num: int) -> str:
        digitString = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        result = ""
        if num > 99:
            result += digitString[num // 100] + " Hundred "
        
        num %= 100
        if num < 20 and num > 9:
            result += teenString[num - 10] + " "
        else:
            if num >= 20:
                result += tenString[num // 10] + " "
            num %= 10
            if num > 0:
                result += digitString[num] + " "
        
        return result
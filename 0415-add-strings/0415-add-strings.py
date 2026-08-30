class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # return str(int(num1) + int(num2))
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = ""
        while i >= 0 or j >= 0 or carry:
            digit1 = 0
            digit2 = 0
            if i >= 0:
                digit1 = int(num1[i])
            if j >= 0:
                digit2 = int(num2[j])
            total = digit1 + digit2 + carry
            carry = total // 10
            remainder = total % 10
            result = str(remainder) + result
            i -= 1
            j -= 1
        return result
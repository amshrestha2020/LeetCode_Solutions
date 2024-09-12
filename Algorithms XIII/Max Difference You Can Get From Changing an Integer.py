class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        a = b = str_num

        # For 'a', replace the first non-nine digit from the left with nine
        for digit in str_num:
            if digit != '9':
                a = a.replace(digit, '9')
                break

        # For 'b', replace the first non-one and non-zero digit from the left with one
        # If the first digit is one, replace the first digit from the left that is greater than one and is not equal to the first digit with zero
        if str_num[0] != '1':
            b = b.replace(str_num[0], '1')
        else:
            for digit in str_num[1:]:
                if digit != '0' and digit != '1':
                    b = b.replace(digit, '0')
                    break

        return int(a) - int(b)

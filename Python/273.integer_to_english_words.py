#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/21/18 9:13 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: 273.integer_to_english_words.py
# @Software: PyCharm


class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        tens = " Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen " \
               "Seventeen Eighteen Nineteen".split()
        twenty = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        hundred = "Hundred"
        thousand = "Thousand Million Billion".split()
        words, digits = [], 0
        while num:
            token, num, word = num % 1000, num // 1000, ''
            if token > 99:
                word += tens[token // 100] + ' ' + hundred + ' '
                token %= 100
            if token > 19:
                word += twenty[token // 10 - 2] + ' '
                token %= 10
            if token > 0:
                word += tens[token] + ' '
            word = word.strip()
            if word:
                word += ' ' + thousand[digits - 1] if digits else ''
                words += word,
            digits += 1
        return ' '.join(words[::-1]) or 'Zero'


if __name__ == '__main__':
    sol = Solution()
    num = 647
    print(sol.numberToWords(num))

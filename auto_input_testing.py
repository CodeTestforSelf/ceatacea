# VScode Extension - Competitive Programming Helper (cph)

# Basic setting & import Libraries
import sys
import re
import datetime

input = sys.stdin.readline()

def longestPalindrome(string):
    string = string.lower()
    length = len(string)
    # check the whole string is palindrome
    if string == string[::-1]:
        return length
    # case like ab, gi len <= 2 not palindrome
    elif length <= 2:
        return length - 1
    # if len(string) < 2:
    #     if string == string[::-1]:
    #         return len(string)
    #     else




string = input
print(longestPalindrome(string))
# longestPalindrome(string)
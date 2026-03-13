"""
Mirror Kingdom Question
Problem Statement:
In the Mirror Kingdom, every message is encrypted using a magical rule: A becomes Z, B becomes Y, C becomes X, and so on (the alphabet is reversed). Every letter in the message is replaced by its mirror alphabet. Given a string representing the original message, help the royal messenger convert it into the mirror cipher message.

Sample Input:
abc

Sample Output:
zyx

"""

s = "abcd"

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for ch in s:
    index = alphabet.index(ch)
    result += alphabet[25 - index]

print(result)
"""
MOST FREQUENT CHARACTER AND FIRST NON REPEATING CHARACTER
TCS NQT Coding Question

Problem Statement:
You are given a string S consisting of lowercase English letters.
Your task is to perform the following operations:

1. Find the first non-repeating character in the string.
   - If no such character exists, print None.

2. Find the most frequent character in the string.
   - If multiple characters have the same highest frequency, print the one that appears first in the string.
   - If all characters occur only once, print the first character of the string.

Input Format:
A single line containing a string S.

Output Format:
Print two lines:
1. First non-repeating character.
2. Most frequent character.

Constraints:
1 ≤ |S| ≤ 10^5
String contains only lowercase English letters.

Sample Input:
uzaifansari

Sample Output:
u
a

Explanation:
Frequency of characters in "uzaifansari":
u -> 1
z -> 1
a -> 3
i -> 2
f -> 1
n -> 1
s -> 1
r -> 1

The first non-repeating character is 'u'.
The most frequent character is 'a'.
"""

from collections import Counter

# s = "uzaifansari"
s = input()
freq = Counter(s)

# First non repeating character
first = None
for ch in s:
    if freq[ch] == 1:
        first = ch
        break
print(first if first else None)
# print(f"{first} is the first non repeating character" if first else None)

# Most frequent character
max_freq = max(freq.values())
if max_freq == 1:
    print(s[0])
    # print(f"{s[0]} is the first character of the string since there is no repeated character")
else:
    for ch in s:
        if freq[ch] == max_freq:
            print(ch)
            # print(f"{ch} is the most frequently repeated character with {max_freq} repititions")
            break
# bonus methods
# print(freq.most_common(1)) #full tuple
# print(freq.most_common(1)[0][0]) #character only
# print(freq.most_common(1)[0][1]) #frequency only
# print(len(freq)) #will print unique elements as the counter stores only unique keys

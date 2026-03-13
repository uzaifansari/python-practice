"""
VALID PAIRS OF THE ARRAY
TCS NQT Coding Question

Problem Statement:
You are given an array of integers of size N and two integers X and Y
representing a range.

Your task is to count the number of valid pairs (i, j) such that when
the elements arr[i] and arr[j] are concatenated, the resulting number
lies within the range [X, Y].

Concatenation means joining the digits of the two numbers.
For example:
If arr[i] = 2 and arr[j] = 5, concatenation = 25.

Input Format:
First line: Integer N representing the number of elements in the array.
Second line: Integer X representing the lower limit of the range.
Third line: Integer Y representing the upper limit of the range.
Next N lines: Elements of the array.

Output Format:
Print the total number of valid pairs.

Constraints:
1 ≤ N ≤ 100
0 ≤ arr[i] ≤ 1000
0 ≤ X ≤ Y ≤ 10^9

Sample Input:
5
20
50
2
5
7
6
3

Sample Output:
10

Explanation:
Array = [2, 5, 7, 6, 3]

Possible concatenations:
22, 25, 27, 26, 23
52, 55, 57, 56, 53
72, 75, 77, 76, 73
62, 65, 67, 66, 63
32, 35, 37, 36, 33

Valid numbers within range [20, 50]:
22, 25, 27, 26, 23, 32, 35, 37, 36, 33

Total valid pairs counted according to the logic of the program.
"""

n = int(input())
x = int(input())
y = int(input())

arr = []
for i in range(n):
    elem = int(input())
    arr.append(elem)

valid_pairs = 0

for i in range(n):
    for j in range(n):
        concatenated = str(arr[i]) + str(arr[j])
        concatenated = int(concatenated)
        if concatenated >= x and concatenated <= y:
            valid_pairs += 1
            
print(valid_pairs)

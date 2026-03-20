"""
**Problem Title:** Move All Zeros to the End

**Problem Statement:**
You are given an array of integers of size **N**. Your task is to move all the zeros in the array to the **end**, while maintaining the relative order of the non-zero elements.

---

**Input Format:**

* The first line contains an integer **N**, the size of the array.
* The second line contains **N** space-separated integers representing the array elements.

---

**Output Format:**

* Print the modified array such that all zeros are moved to the end, while preserving the order of non-zero elements.

---

**Constraints:**

* 1 ≤ N ≤ 10^5
* -10^9 ≤ array elements ≤ 10^9

---

**Example:**

**Input:**
8
4 5 0 1 9 0 5 0

**Output:**
4 5 1 9 5 0 0 0

---

**Explanation:**
The array contains three zeros. After moving all zeros to the end while maintaining the order of non-zero elements, the resulting array is:
4 5 1 9 5 0 0 0

"""
# space seperated array VERY IMPORTANT
# arr = list(map(int, input().split())) # 4 5 0 1 9 0 5 0
# comma seperated array VERY IMPORTANT
arr = list(map(int, input().split(','))) # 4,5,0,1,9,0,5,0

zero = []
non_zero = []

for ch in arr:
    if ch == 0:
        zero.append(ch)
    else:
        non_zero.append(ch)
print(*(non_zero+zero))

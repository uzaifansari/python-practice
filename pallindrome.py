# PALLINDROME OR NOT
s = 'racecar'
rev = ""

for ch in s:
    rev = ch + rev

print("pallindrome" if rev==s else "not a pallindrome")

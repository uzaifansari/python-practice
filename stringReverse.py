# REVERSING A STRING
name = str(input("Enter your name: "))

# Method 1
reverse_name = ""

for char in name:
    # u + "" = u,
    # z + u = zu,
    # a + zu = azu 
    # i + azu = iazu 
    # f + iazu = fiazu 
    reverse_name = char + reverse_name

#Method 2
reverse_name = "".join(reversed(name))

print(reverse_name)

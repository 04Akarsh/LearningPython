# 🧵 STRING SLICING

# Let's start with a string
text = "Hello, Python!"

# 🔤 Basic slicing: string[start:stop]
print(text[0:5])   # ➜ 'Hello' (from index 0 to 4)

# ⏩ Slicing with step
print(text[0:13:2])  # ➜ 'Hlo yhn' (every 2nd character)

# 🪞 Reverse the string
print(text[::-1])  # ➜ '!nohtyP ,olleH'

# 💬 Negative slicing
print(text[-7:-1])  # ➜ 'Pytho' (starts from -7 to -2)

print("---")  # Separator for clarity in output

# LIST SLICING

# Let's create a sample list
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# Basic slicing: list[start:stop]
print(numbers[1:4])  # ➜ [20, 30, 40]

# Omit start index
print(numbers[:3])   # ➜ [10, 20, 30]

# Omit stop index
print(numbers[4:])   # ➜ [50, 60, 70, 80]

# ▶️ INDEXING EXPLAINED:
# Each character in a string has an index:
#  Positive indexing (left to right):
#   H  e  l  l  o  ,     P  y  t  h  o  n  !
#   0  1  2  3  4  5  6  7  8  9 10 11 12 13
#
#  Negative indexing (right to left):
#  H   e   l   l   o   ,       P   y   t   h   o   n   !
# -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
# 🪞 Reversing the string using slicing / Negative indices
# Here's how it works:
# Syntax: string[start:stop:step]
# When step is -1:
#   - It tells Python to move **backwards** through the string.
#   - `start` and `stop` can be left empty — Python will:
#       - Start from the end (`-1` index, which is the last character)
#       - Go backward until it passes the beginning
# So, text[::-1] means:
#   - Start from the last character
#   - Move one character at a time in reverse
#   - Stop when you've passed the start of the string 
print(numbers[-3:])  # ➜ [60, 70, 80]
print(numbers[:-2])  # ➜ [10, 20, 30, 40, 50, 60]

# Add step: list[start:stop:step]
print(numbers[0:8:2])  # ➜ [10, 30, 50, 70]

# Reverse the list
print(numbers[::-1])   # ➜ [80, 70, 60, 50, 40, 30, 20, 10]

# Every 3rd element
print(numbers[::3])    # ➜ [10, 40, 70]

# Confirm original list is unchanged
print("Original list:", numbers)

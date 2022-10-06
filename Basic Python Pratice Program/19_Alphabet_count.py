"""
input : Wubba Lubba Dub Dub
output : {'W': 1, 'u': 4, 'b': 6, 'a': 2, ' ': 3, 'L': 1, 'D': 2}
"""
text = ("Wubba Lubba Dub Dub")
dict = {}
for char in text:
    if char in dict:
        dict[char] += 1
    else:
       dict[char] = 1
print(dict)
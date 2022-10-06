"""
input : eye
output : eye is palindrome
"""
s=input("enter first string\n")
if s==s[::-1]:
    print(s,"is palindrome")
else :
    print(s,"is not a palindrome")
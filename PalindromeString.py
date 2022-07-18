Name = input()
print(Name[::-1])
if Name == Name[::-1]:
    print("it's a palindrome")
else:
    print("it isn't a palindrome")
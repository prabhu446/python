user_input = input("Please enter an input:")
# ::-1 will put the given string/number in reverse
reverse = user_input[::-1]
print(reverse)
if reverse == user_input:
    print("Given input is Palindrome")
else:
    print("Given input is not a Palindrome")

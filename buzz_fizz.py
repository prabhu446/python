# If a number is divisible by 3, print buzz
# If a number is divisible by 5, print fizz
# If a number is divisible by both 3 and 5, print buzzfizz
# If a number is NOT divisible by 3 and 5 then print just the given number.

# There is no need to write else or elseif as a contional statement after if statement, we can directly return the output if the condition is not met.
# Below I used only if conditions 3 times and finally if none of the 3 if statements are met then finally return the result as elseif statement.

def buzz_fizz(user_input):
    if user_input % 3 == 0 and user_input % 5 == 0:
        return "buzzfizz"
    if user_input % 3 == 0:
        return 'buzz'
    if user_input % 5 == 0:
        return 'fizz'
    return user_input


print(buzz_fizz(15))

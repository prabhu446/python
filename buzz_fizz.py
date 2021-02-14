# If a number is divisible by 3, print buzz
# If a number is divisible by 5, print fizz
# If a number is divisible by both 3 and 5, print buzzfizz
# If a number is NOT divisible by 3 and 5 then print just the given number.


def buzz_fizz(user_input):
    if user_input % 3 == 0 and user_input % 5 == 0:
        return "buzzfizz"
    if user_input % 3 == 0:
        return 'buzz'
    if user_input % 5 == 0:
        return 'fizz'
    return user_input


print(buzz_fizz(15))

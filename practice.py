"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


def hello_world():
    """
    Prints "Hello World"
    """

    print "Hello World"


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


def say_hi(name_string):
    """
    Takes a name as a string and prints "Hi" followed by the name
    """

    if type(name_string) is str:
        print "Hi %s" % (name_string)

# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.


def print_product(integer1, integer2):
    """
    Takes two integers and multiplies them, then prints the result.
    """

    if type(integer1) is int and type(integer2) is int:
        print integer1 * integer2


# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times


def repeat_string(str_to_repeat, num_times):
    """
    Takes a string and an integer and prints the string that many times
    """

    if type(str_to_repeat) is str and type(num_times) is int:
        print str_to_repeat * num_times


# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".


def print_sign(any_integer):
    """
    Takes an integer and prints if it is higher than, lower than, or is 0

    Expected results are "Higher than 0", "Lower than 0", "Zero"
    """

    if type(any_integer) is int:

        if any_integer > 0:
            print "Higher than 0"
        elif any_integer == 0:
            print "Zero"
        else:
            print "Lower than 0"


# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


def is_divisible_by_three(any_integer):
    """
    Tests if an integer is divisible by is divisible by 3

    Takes an integer and returns True if divisible by 3 and False if not
    """

    if type(any_integer) is int:
        if any_integer % 3 == 0:
            return True

        return False


# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(any_string):
    """
    Returns number of spaces in a string
    """

    if type(any_string) is str:
        space_count = 0
        for character in any_string:
            if character == " ":
                space_count += 1

        return space_count


# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(meal_price, tip=0.15):
    """
    Calculates meal price including tip.

    Defaults with a tip of 15%.
    """
    return meal_price + meal_price * tip

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.


def sign_and_parity(any_integer):
    """
    Returns a list of two pieces of information as strings for any integer.

    It will return 'Positive' or 'Negative' for the first item and 'Even' or
    'Odd' for the second item.
    """

    if type(any_integer) is int:
        sign_and_parity_list = []

        if any_integer % 2 == 0:
            sign_and_parity_list.append("Even")
        else:
            sign_and_parity_list.append("Odd")

        if any_integer >= 0:
            sign_and_parity_list.append("Positive")
        else:
            sign_and_parity_list.append("Negative")

        return sign_and_parity_list

    parity, sign = sign_and_parity(-20)



################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


def full_title(name, job_title="Engineer"):
    """
    Returns job title and name as one string.

    Default job title is an Engineer.
    """
    if type(name) is str and type(job_title) is str:
        return job_title + ' ' + name


def write_letter(recipient_name, recipient_title, sender_name):
    """
    Prints a letter
    """
    if type(recipient_name) is str and type(recipient_title) is str\
            and type(sender_name) is str:

        full_title_str = full_title(recipient_name, recipient_title)

        print "Dear %s, I think you are amazing! Sincerely, %s" % \
            (full_title_str, sender_name)



#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

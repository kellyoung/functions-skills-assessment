# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def add_tax_to_cost(item_cost, state_abbrev, tax_rate=0.05):
    """
    Returns cost including tax.

    Defaults to (5%) tax and automatically calculates (7%) tax
    if state abbreviation parameter is California.
    """
    if state_abbrev == "CA":
        tax_rate = 0.07

    total_cost = item_cost + item_cost * tax_rate
    return total_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".

def is_berry(fruit_name):
    """
    Returns True if fruit is a strawberry, cherry, or blackberry.

    False otherwise.
    """
    fruit_possibilities = ["strawberry", "cherry", "blackberry"]

    if fruit_name in fruit_possibilities:
        return True

    return False

    """
    ALTERNATIVE

    if fruit_name == "strawberry" or fruit_name == "strawberry" or
            fruit_name == "blackberry":
        return True

    return False
    """

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit_name):
    """
    Calculates shipping cost depending on if fruit_name is a berry or not.

    Calls the function is_berry() to determine whether or not the fruit
    is a berry.
    """

    if is_berry(fruit_name):
        return '0'

    return '5'

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.


def is_hometown(town_name):
    """
    Takes a town's name and returns True if the town name is 'Irvine'
    """

    town_name = town_name.upper()

    if town_name == "IRVINE":
        return True

    return False


#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first_name, last_name):
    """
    Takes a first_name and last_name and returns it as one string
    """

    if type(first_name) is str and type(last_name) is str:
        return "%s %s" % (first_name, last_name)


#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################
"""
The function `is_negative` below is implemented correctly - it returns True if the given number is negative and False otherwise.

However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by *75%* while keeping the same behaviour. 

See if you can come up with an equivalent body that uses just **one line** of code, and put it in the function `concise_is_negative`. 

"""

def is_negative(number):
    if number < 0:
        return True
    else:
        return False
print(is_negative(-1))
"""
to be
"""
def concise_is_negative(number):
    return number < 0
print(concise_is_negative(1))
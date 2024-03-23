"""
Example - Multiple "elif" statements¶
So far, you have seen "elif" used only once in a function. But there's no limit to the number of "elif" statements you can use. For instance, the next block of code calculates the dose of medication (in milliliters) to give to a child, based on weight (in kilograms).

Note: This function should not be used as medical advice, and represents a fake medication
"""

def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose

"""
The next code cell runs the function. Make sure that the output makes sense to you!

In this case, the "if" statement was False, and all of the "elif" statements evaluate to False, until we get to weight < 15.9, which is True, and dose is set to 5.
Once an "elif" statement evaluates to True and the code block is run, the function skips over all remaining "elif" and "else" statements. After skipping these, all that is left is the return statement, which returns the value of dose.
The order of the elif statements does matter here! Re-ordering the statements will return a very different result.
"""

print(get_dose(12))

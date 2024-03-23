"""
Conditional statements
Conditional statements use conditions to modify how your function runs. They check the value of a condition, and if the condition evaluates to True, then a certain block of code is executed. (Otherwise, if the condition is False, then the code is not run.)

You will see several examples of this in the following sections.

"if" statements
The simplest type of conditional statement is an "if" statement. You can see an example of this in the evaluate_temp() function below. The function accepts a body temperature (in Celcius) as input.

Initially, message is set to "Normal temperature".
Then, if temp > 38 is True (e.g., the body temperature is greater than 38°C), the message is updated to "Fever!". Otherwise, if temp > 38 is False, then the message is not updated.
Finally, message is returned by the function.
"""

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))
print(evaluate_temp(39))


"""
Note that there are two levels of indentation:

The first level of indentation is because we always need to indent the code block inside a function.
The second level of indentation is because we also need to indent the code block belonging to the "if" statement. (As you'll see, we'll also need to indent the code blocks for "elif" and "else" statements.)
Note that because the return statement is not indented under the "if" statement, it is always executed, whether temp > 38 is True or False.
"""
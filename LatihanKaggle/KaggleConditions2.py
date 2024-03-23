"""
"if ... else" statements
We can use "else" statements to run code if a statement is False. 
The code under the "if" statement is run if the statement is True, and the code under "else" is run if the statement is False.
"""

def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(37))

"""
In the code cell below, we run the code under the "elif" statement, because temp > 38 is False, and temp > 35 is True. 
Once this code is run, the function skips over the "else" statement and returns the message.
"""

print(evaluate_temp_with_elif(36))

"""
Finally, we try out a case where the temperature is less than 35°C.
Since the conditionals in the "if" and "elif" statements both evaluate to False, the code block inside the "else" statement is executed.
"""

print(evaluate_temp_with_elif(34))

""" 'Low temperature.' """
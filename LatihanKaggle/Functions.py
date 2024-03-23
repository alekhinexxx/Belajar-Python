# Define the function
def add_three(input_var):
    output_var = input_var + 3
    return output_var

new_number = add_three(10)

# Check that the value is 13, as expected
print(new_number)

def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

# Calculate pay based on working 40 hours
pay_fulltime = get_pay(40)
print(pay_fulltime)

pay_parttime = get_pay(32)
print(pay_parttime)

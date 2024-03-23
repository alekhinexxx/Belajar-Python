test_value = 2.17

rounded_value = math.ceil(test_value)
print(rounded_value)

def round_up_and_divide_by_three(num):
    new_value = math.ceil(num)
    final_value = new_value / 3
    return final_value

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    gallons_to_buy = math.ceil(gallons_needed)
    cost = cost_per_gallon * gallons_to_buy
    return cost

print(get_actual_cost)
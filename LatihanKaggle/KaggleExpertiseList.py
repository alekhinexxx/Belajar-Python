# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
total = len(num_customers)
avg_first_seven = sum(num_customers[7:])/len(num_customers)
avg_last_seven = sum(num_customers[:7])/len(num_customers)
max_month = max(num_customers)
min_month = min(num_customers)


print(total)
print(avg_first_seven)
print(avg_last_seven)
print(max_month)
print(min_month)
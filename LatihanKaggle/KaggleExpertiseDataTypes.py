#jika tidak memiliki basement maka false

def get_expected_cost(beds, baths, has_basement):
    boolen = has_basement * 4000
    value = 8000 + 3000 * beds + 10000 * baths, (boolen > 3999)  
    return value


hasil = get_expected_cost(1,1,0)

print(hasil)
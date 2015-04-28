def hotel_cost(nights):   '''Hotel costs fixed at 140 and is multiplied by the number of nights'''
    return 140 * nights
    
def plane_ride_cost(city):  '''Flight costs which may depend on the city......included 3 cities'''
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):  '''Car rental costs have some conditons themselves'''
    rent = 40 * days
    if days >= 7:
        rent = rent - 50
    elif days >= 3:
        rent = rent - 20
    return rent

def trip_cost(city, days, spending_money):  '''calculating the total cost including some spending money'''
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money

print trip_cost("Los Angeles", 5 , 600)

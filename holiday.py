#Def hotel_cost to calculate the total hotel cost
def hotel_cost(num_nights, city_hotel): 
    if city_flight == "1":
        city_hotel = 90
        hotel_cost = int(num_nights) * city_hotel
        return hotel_cost
    
    if city_flight == "2":
        city_hotel = 150
        hotel_cost = int(num_nights) * city_hotel
        return hotel_cost
    
    if city_flight == "3":
        city_hotel = 105
        hotel_cost = int(num_nights) * city_hotel
        return hotel_cost
    
    if city_flight == "4":
        city_hotel = 130
        hotel_cost = int(num_nights) * city_hotel
        return hotel_cost

#Def plane_cost to define the flight cost for each city
def plane_cost(plane):
    if city_flight == "1":
        plane = 75
        return plane
    
    if city_flight == "2":
        plane = 70
        return plane
    
    if city_flight == "3":
        plane = 80
        return plane
    
    if city_flight == "4":
        plane = 60
        return plane

#Def car_rental to calculate the total cost of renting a car    
def car_rental(rental_days, rental_per_day = 50):
    car_rental = int(rental_days) * rental_per_day
    return car_rental

#Def site to give name of city depending on number inserted by user
def site(city):
    if city_flight == "1":
        city = "Barcelona"
        return city
    
    if city_flight == "2":
        city = "Amsterdam"
        return city
    
    if city_flight == "3":
        city = "Rome"
        return city
    
    if city_flight == "4":
        city = "Paris"
        return city

#Def holiday_cost to calculate the total cost of the holidays
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = hotel_cost(num_nights, city_flight) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

while True:
    print("Barcelona: 1 \nAmsterdam: 2 \nRome: 3 \nParis: 4")
    
    city_flight = input("From the above options insert the number of the city that would like to flight: ")
    
    if city_flight in ("1", "2", "3", "4"):     #Choose destination city
        
        try:
            num_nights = int(input("Please enter the number of nights that you will stay: "))     #Insert number of nights that user will stay
            rental_days = int(input("Please enter the days that you will hire a car: "))     #Insert number of days that will hire a car
        
        except Exception:
            print("\nInvalid input. Please insert a whole number.\n")
            continue

        #Prints out the cost details of the destination choosen by user
        if city_flight in ("1", "2", "3", "4"):
            print(f"\nYou have choosen {site(city_flight)} as your destination. The total costs are the following:")
            print(f"\nFor {num_nights} night/s the hotel cost is: £{hotel_cost(num_nights, city_flight)}")
            print(f"The costs of the flight is: £{plane_cost(city_flight)}")
            print(f"The cost of car rental for {rental_days} day/s is: £{car_rental(rental_days)}")

            print(f"\nThat makes a total cost of: £{holiday_cost(hotel_cost, plane_cost, car_rental)}")
        
        #Ask user if would like to insert a different city destination
        next_flight = input("\nIf you would like to calculate another destination press any key or insert 'no' to exit: ").capitalize()
        
        #If user inserts 'no' the program the while loop will stop
        if next_flight == "No":
            break

    #Prints out a message if user inserted a different option than '1', '2', '3' or '4'    
    else:
        print("\nInvalid input. Please make sure that you insert '1', '2', '3', or '4'\n")



        



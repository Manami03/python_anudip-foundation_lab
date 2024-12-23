#5. A transport company charges the fare according to following table:
#Distance Charges
#1-50 	8 Rs./Km
#51-100 	10 Rs./Km
#> 100 	12 Rs/Km


distance = float(input("Enter the distance (in km): "))
if distance >= 1 and distance <= 50:
    fare = distance * 8  
elif distance > 50 and distance <= 100:
    fare = distance * 10  
else:
    fare = distance * 12  
print(f"The total fare for {distance} km is: {fare} Rs.")

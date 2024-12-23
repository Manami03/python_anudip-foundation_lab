
#Write a program to input distance travelled as input and calculate and print the total charge.
#Use comments where necessary and follow python naming conventions.

distance = float(input("Enter the distance travelled (in kilometers): "))
charge_per_km = 5
total_charge = distance * charge_per_km
print(f"The total charge for {distance} km is: {total_charge} currency units.")

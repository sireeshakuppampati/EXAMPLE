#Program to generate and calculate the total invoice 
#for EDSEL CAR COMPANY
#Date written : Sept 17 2023
#Author : SIREESHA KUPPAMPATI

#Entering the input values
CustName = input("Enter the Customer Name: ")
CustPhNum = input("Enter the Customer Phone Number :  ")
NumDays = input("Enter the Number of Days Rented:  ")
NumDays = int(NumDays)
OdomtrBef = input("Enter the Odometer Reading before Renting: ")
OdomtrBef = int(OdomtrBef)
OdomtrAft = input("Enter the Odometer Reading after Renturning: ")
OdomtrAft = int(OdomtrAft)

#Declaring Constant Values
CAR_RATE = 55
KILO_RATE = 0.24
InsCost = 14
RentDiscount = 0.10
MilDiscount = 0.25
HST_RATE = 0.15


#Required Calculation Part
TotKilos = OdomtrAft - OdomtrBef
RentalCost  = NumDays * CAR_RATE
MileageCost =  TotKilos * KILO_RATE

#Calculating the Insurance Cost per day
TotInsuranceCost = NumDays * InsCost

#Calculating the Discount during summer as
#10% on RentalCost and 25% on Total Mileage
TotRentDiscount = RentalCost * RentDiscount
TotMilDiscount = MileageCost * MilDiscount
TotDiscount = TotRentDiscount + TotMilDiscount

#Calculating TotalCost and HST
TotalCost = (RentalCost + MileageCost + TotInsuranceCost) - TotDiscount
HST = TotalCost * HST_RATE

#Finally Calculating the FinalInvoice
FinalInvoice = TotalCost + HST

#Printing USer Display of Results
print()
print("Customer Nmae:                           ",                              CustName)
print("Customer phone Number:                   ",                      CustPhNum)
print("Number of Days Customer Rented the CAR:  ",     NumDays)
print("Total Kilometers the Customer Travelled: ",    TotKilos)
print("Total Rental Cost:                       ",                          RentalCost)
print("Total Mileage Cost:                      ",                         MileageCost)
print("Total Insurance Cost for Customer:       ",          TotInsuranceCost)
print("Total RentalDiscount is:                 ",                    TotRentDiscount)
print("Total Nileage Discount:                  ",                     TotMilDiscount)
print("Total Discount is:                       ",                          TotDiscount)
print("Total Amount on CAR Rental:              ",                   TotalCost)
print("HST Amount:                              ",                                 HST)
print()
print("Final Invoice :                          ",                             FinalInvoice)







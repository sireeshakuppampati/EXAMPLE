#[10-12 1:57 p.m.] Maurice Babin
#Program for Thursday working with dates.


# Comment like a pro.
 
import datetime
 

# Define the current date and print with different formats
 
CurDate = datetime.datetime.now()  # Grab the current date from the system date.
 
print()
print("Current date based on the system date")
print("Note how it prints the date and time")
print(CurDate)
 
print()
print("Different formats when printing out a date")
print(CurDate.strftime("%A %a %Y %y %m %B %b %d"))
 
CurDateDsp = CurDate.strftime("%B %d, %Y")
print(CurDateDsp)
 
print(CurDate.strftime("%Y/%m/%d"))
print(CurDate.strftime("%B %d, %Y"))
print(CurDate.strftime("%A %B %d, %Y"))


 
# Add 4 days and 30 days to the Current date
CurDatePlus4 = CurDate + datetime.timedelta(days = 4)
print()
print("Current date plus 4 days")
print(CurDatePlus4)
 
CurDatePlus30 = CurDate + datetime.timedelta(days = 30)
print()
print("Current date plus 30 days")
print(CurDatePlus30)


 
# Define two dates as strings - same as if these were input
arrivalstr = "2021-2-3" # input("Enter the arrival date (YYYY-MM-DD): ")
departurestr = "2021-2-6"
 
# Convert the arrival and departure from string objects to datetime objects
arrival = datetime.datetime.strptime(arrivalstr, "%Y-%m-%d")
print()
print("Arrival date converted from string object to datetime object")
print(arrivalstr)
print(arrival)
 
departure = datetime.datetime.strptime(departurestr, "%Y-%m-%d")
print()
print("Departure date converted from string object to datetime object")
print(departure)
 
# Calculate the number of days between the two dates
days = (departure - arrival).days
print()
print("Difference between arrival and departure date in days")
print(days)
 
# Pull out the different parts of a date and create a new date
CurYear = CurDate.year
print()
print("Parts of a date including the Year, Month and Day from CurDate")
print(CurYear)
CurMonth = CurDate.month
print(CurMonth)
CurDay = CurDate.day
print(CurDay)
 
# Create a new date using the tear, month and day components
New = datetime.date(CurYear, CurMonth, CurDay)
print(New)
 
# New date one month earlier
NewLessAMonth = datetime.date(CurYear, CurMonth - 1, CurDay)
print(NewLessAMonth)
 
# New date one year, 2 months, and 4 days in the future
NewFuture = datetime.date(CurYear + 1, CurMonth + 2, CurDay + 4)
print(NewFuture)

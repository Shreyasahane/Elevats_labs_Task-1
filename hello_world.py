# import datetime to get todays date
import datetime

# taking name from user
name = input("Enter your name: ") 

#taking Internship name that have been selected
role =input("Enter Internship Role:")

#display Todays date
Today_date = datetime.date.today()

# for displaying the user details as name, internship name and todays date
print("Name: ",name)
print("Internship Name: ",role)
print("Todays Date: ",Today_date)
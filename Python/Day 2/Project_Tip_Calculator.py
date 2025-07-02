Total_Bill = float(input("Enter the total bill : $"))
Tip_percentage = int(input("How much (%) tip would you like to give? : "))
Number_of_people = int(input("How many people to split the bill : "))

each_person_bill = (Total_Bill + (Total_Bill * (Tip_percentage/100)))/Number_of_people

print(f"Each person should pay : {round(each_person_bill,2)}")
#imports the math module
import math
 
#declares the variables used in the selection of calculation and interest type
calcType = 0
intType = 0
 
#allows the user to choose what they would like to calculate
#number selection used in place of "investment/bond" manual input to reduce chance of user error
while(calcType == 0):
    select = input("Please select which you would like to calculate 1) Investment / 2) Bond): ")
     
    #determines if the user is calculating an investment or a bond
    if(select == "1"):
        calcType = 1
    elif(select == "2"):
        calcType = 2
    else:
        print("Please only select option 1 or 2.")
 
#allows the user to input the information that will be used to calculate their investment total
if(calcType == 1):
    amount = float(input("Investment amount: "))
    rate = float(input("Rate: "))
    rate = rate * 0.01
    term = int(input("Term (years): "))
 
    #allows the user to select simple or compound interest
    #number selection used in place of "simple/compound" manual input to reduce chance of user error
    while(intType == 0):
        selectInt = input("Please select your interest rate type 1) Simple / 2) Compound): ")
 
        #determines if the user is using simple or compound interest
        if(selectInt == "1"): 
            intType = 1
        elif(selectInt == "2"): 
            intType = 2
        else:
            print("Please only select option 1 or 2.")
     
    #calculates the interest based on the above selection using appropriate formulas
    if(intType == 1):
        interest = (amount * (1 + rate * term))
    elif(intType == 2): 
        interest = (amount * math.pow((1 + rate), term))
     
    #prints the total of the calculation based on the users input
    print(f"Total after {term} years: R{round(interest, 2)}")
 
#allows the user to input the information that will be used to calculate their total bond repayment
if(calcType == 2):
    amount = float(input("Present value of property: "))
    rate = float(input("Rate: "))
    rate = (rate * 0.01) / 12
    term = float(input("Repayment term (months): "))
 
    #calculates the total bond repayment
    repayment = amount * (rate * (1 + rate) ** term) / ((1 + rate) ** term - 1)
 
    #prints the total bond using the input information
    print(f"Monthly repayment: {round(repayment, 2)}")
    print(f"Total bond: {round(term * repayment, 2)}")
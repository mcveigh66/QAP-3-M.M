# Description: # Honest Harry's car lot sales trackr 
# Author: Megan McVeigh
# Date(s): November, 12th 2025

# Define required libraries.
import datetime 
from FormatValues import * 

# Define program constants.
HST_RATE = 0.15 
LICENCE_FEE_LOW = 75.00
LICENCE_FEE_HIGH = 165.00
TRANS_FEE_RATE = 0.01
LUX_TAX_RATE = 0.016
FIN_FEE_PER_YEAR = 39.99
MAX_SELLING_PRICE = 50000.00

# Define program functions.

# Format the 10 digit phone number as (xxx) xxx-xxxx
def FormatPhone(Phone):
    return f"({Phone[0:3]}) {Phone[3:6]}-{Phone[6:]}"


# Creates format for the receipt
def GenerateReceipt(FirstName, LastName, PlateNum, Phone):
    Initials = FirstName[0].upper() + LastName[0].upper()
    LastThreePlate = PlateNum[-3:]
    LastFourPhone = Phone[-4:]
    return f"{Initials}-{LastThreePlate}-{LastFourPhone}"

# Calculating all the fees, taxes and price total 
def CalcFees(SellPrice, TradeIn):
    PriceAfter = SellPrice - TradeIn 
    LicenceFee = LICENCE_FEE_LOW if SellPrice <= 15000 else LICENCE_FEE_HIGH

    TransFee = SellPrice * TRANS_FEE_RATE
    if SellPrice > 20000:
        TransFee += SellPrice * LUX_TAX_RATE

    Subtotal = PriceAfter + LicenceFee + TransFee
    HSTFee = Subtotal * HST_RATE
    Total = Subtotal + HSTFee

    return PriceAfter, LicenceFee, TransFee, Subtotal, HSTFee, Total

# Calculating the Pay Schedule for 1-4 months 
def CalcPaySchedule(TotSalePrice):
    Schedules = []

    for Years in range(1, 5):
        Months = Years * 12
        Fin_Fee = FIN_FEE_PER_YEAR * Years
        TotalPrice = TotSalePrice + Fin_Fee
        MonthlyPay = TotalPrice / Months

        Schedules.append([
            Years,
            Months,
            Fin_Fee,
            TotalPrice,
            MonthlyPay
        ])

    return Schedules


# Main program starts here.
while True:
    print()
    print()
    print("Welcome to Used Harry's Car Lot Sales Tracker:   ")
    print()
    print()
    
    # Gather user inputs.   
    while True:
        FirstName = input("Enter the customer first name (or 'END' to quit):                        ").strip().title()
        
        if FirstName.upper() == "END":
            print("Exiting Program. Goodbye.")
            break

        if FirstName == "":
            print("First name cannot be empty.")
            continue 

        break
        

    LastName =    input("Enter the customer last name:                                            ").strip().title()
    while not LastName:
        LastName = input("Last name cannot be empty:                                              ").strip()

    while True:
        Phone =   input("Enter the 10-digit phone number:                                         ").strip()
        if (Phone.isdigit() and len(Phone) == 10):
            break
        else:
            print("Invalid. Enter 10-digit phone number (Numbers Only)")
    

    while True:
        Plate =   input("Enter the plate number (XXXXXX):                                         ").strip()
        if len(Plate) == 6:
            break
        else: 
            print("Invalid. Enter a valid plate number                                            ")

    CarMake =     input("Enter Car Make:                                                          ").strip().title()
    CarModel =    input("Enter Car Model:                                                         ").strip().title()
    Year =        input("Enter the car year:                                                      ").strip()

    SellingPrice = float(input("Enter selling price less than 50,000:                                    "))
    while SellingPrice > MAX_SELLING_PRICE:
        SellingPrice = float(input("Too high. Enter selling price less than 50,000:                      "))

    TradeIn = float     (input("Enter the trade in amount (Must be less than selling price):             "))
    while TradeIn > SellingPrice: 
        TradeIn = float(input("Invalid. Enter Trade-In Amount that is less than selling price.           "))

    SalePerson =         input("Enter the Salesperson name:                                              ").strip().title()
    while not SalePerson:
        SalePerson = input("SalesPersons name cannot be empty:                                           ")

         
    # Perform required calculations.
    ReceiptID = GenerateReceipt(FirstName, LastName, Plate, Phone, )
    InvDate = datetime.date.today().strftime("%B %d, %Y")
    PriceAfter, LicFee, TransFee, SubTot, HST, Total = CalcFees(SellingPrice, TradeIn)

    # Display results

    print()
    print()
    print(f"Honest Harry Car Sales".ljust(40) + f"Invoice Date: {InvDate}")
    print(f"Used Car Sale and Receipt".ljust(40) + f"Receipt No: {ReceiptID}")
    print()

    print(f"Sold to:                              {'Sale price:':>9s}           {FDollar2(SellingPrice):>10} ")

    print(f"                                      {'Trade Allowance:':>14s}      {FDollar2(TradeIn):>10}")
    print("                                      " + ("-" * 33))

    print(f" {FirstName[:0]} {LastName}                             {'Price after Trade:':>15s}    {FDollar2(PriceAfter):>10}")
    print(f"  {Phone}                          {'License Fee:':>11s}       {FDollar2(LicFee):>10}")
    print(f"                                      {'Transfer Fee:':>12s}      {FDollar2(TransFee):>10}")
    print("                                      " + ("-" * 33))

    print(f"Car Details:                          {'Subtotal:':>9s}             {FDollar2(SubTot):>10}")
    print(f"                                      {'HST:':>4s}                 {FDollar2(HST):>10}")
    print(f"{Year} {CarMake} {CarModel}        ")
    print("                                      " + ("-" * 33))

    print(f"                                      {'Total sales price:':<16s}    {FDollar2(Total):>10}")
    print()
    print("-" * 71)

    PaySchedules = CalcPaySchedule(Total)
    Today = datetime.date.today()

    print(f"{'# Years':<10}{'# Payments':<12}  {'Financing':<15}{'Total':<15}{'Monthly':<15}")
    print(f"{'':<22}  {'Fee':<15}{'Price':<15}{'Payment':<15}")
    print(" --------------------------------------------------------------")
   
    for Yrs, Months, Fee, TotalPrice, Monthly in PaySchedules:
        print(f"  {Yrs:<10}{Months:<12}{FDollar2(Fee):<15}{FDollar2(TotalPrice):<15}{FDollar2(Monthly):<15}")

    FirstPay = Today + datetime.timedelta(days=30)
    if Today.day >= 25:
        FirstPay = Today + datetime.timedelta(days=60)

    print(" --------------------------------------------------------------")
    print(f"First payment date: {FDateM(FirstPay)}")
    print("-" * 70)
    print("                   Best used cars at the best prices!")
    print()
    print()
    print()
    print()


    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.
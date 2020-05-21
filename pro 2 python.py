from math import log, pow, ceil, floor
import argparse
import sys

def main_function():
    parser = argparse.ArgumentParser()
    error = "Incorrect parameters"
    parser.add_argument("--type", type=str, help="the type")
    parser.add_argument("--principal", type=str, help="the principal", default="")
    parser.add_argument("--payment", type=str, help="the payment", default="")
    parser.add_argument("--interest", type=str, help="the interest",default="")
    parser.add_argument("--periods", type=str, help="the periods",default="")
    args = parser.parse_args()
    arg = sys.argv
    if len(arg) != 5:
        print(error)
        return 1
    if args.type not in ("annuity", "diff"):
        print(error)
        return 1
    elif args.type == "annuity":
        typ_short = "a"
    else:
        typ_short = "d"
        if not args.principal  or not args.periods:
            print(error)
            return 1
    
    if args.principal:
        principal = float(args.principal)
    else:
        principal = ""
    if args.payment:
        payment = float(args.payment)
    else:
        payment = ""
    if not args.interest:
        print(error)
        return 1
    else:
        interest = float(args.interest)
        interest = interest / 1200
        
    if args.periods:
        periods = float(args.periods)
    else:
        periods =""
   
    if (payment != "" and payment < 0 ) or (periods != "" and periods < 0 ) or interest < 0  or (principal != "" and principal < 0):
        print(error)
        return 1
    side_function(periods, payment, interest, typ_short, principal)

def side_function(periods, payment, interest, typ_short, principal):  
    dm = 0
    m=0
    if typ_short == "d":
        for i in range(1,int(periods + 1)):
            m = ceil((principal / periods) + interest * (principal-((principal*(i-1))/periods)))
            dm += m
            print(f"Month {i}: paid out {m}")
        print()
        print(f"Overpayment = {dm-principal}")
    else:
        if principal == "":
            principal = payment / (((pow(1+interest, periods) * interest)/(pow(1+interest, periods)-1)))
            print(f"Your credit principal = {principal}!")
            print(f"Overpayment = {(payment*periods)-principal}")
                
        if periods == "":
            periods = ceil(log(payment / (payment - interest * principal), 1 + interest))
            
            years = floor(periods / 12)
            months = periods - (years * 12)
            if years == 0:
                time_years = ""
            elif years == 1 :
                time_years = "1 year"
            else:
                time_years = str(years) + " years"
            if months == 0:
                time_months = ""
            elif months == 1:
                time_months = "1 month"
            else:
                time_months = str(months) + " months"
            print(f"You need {time_years} and {time_months} to repay this credit!")
            print(f"Overpayment = {(payment*periods) - principal}")
                
        if payment == '':
            payment = ((pow(1+interest, periods) * interest) / (pow(1+interest, periods)-1))
            payment = principal * payment
            print(f"Your annuity payment = {ceil(payment)}!")
            print(f"Overpayment = {(ceil(payment)*periods) - principal}")

main_function()

    
            
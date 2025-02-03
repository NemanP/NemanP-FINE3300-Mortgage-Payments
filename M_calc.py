#Mortgage Calculator

def mortgage_payments(princial, rate, amortization):
    # Convert rate into percntage
    r = rate / 100  
    # year to months
    n_monthly = amortization * 12
    
    # Calculate periodic rates
    r_monthly = (1 + r / 2)**(2 / 12) - 1
    r_semi_monthly = (1 + r / 2)**(2 / 24) - 1
    r_bi_weekly = (1 + r / 2)**(2 / 26) - 1
    r_weekly = (1 + r / 2)**(2 / 52) - 1

    # Present Value of Annuity Formula
    def pva(rate, periods):
        return (1 - (1 + rate)**-periods) / rate

    # caluclations
    monthly_payment = principal / pva(r_monthly, n_monthly)
    semi_monthly_payment = principal / pva(r_semi_monthly, n_monthly * 2)
    bi_weekly_payment = principal / pva(r_bi_weekly, n_monthly * 26 / 12)
    weekly_payment = principal / pva(r_weekly, n_monthly * 52 / 12)
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4
    #rounding to 2 decimal places
    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(rapid_bi_weekly_payment, 2),
        round(rapid_weekly_payment, 2)
    )



    # User inputs
principal = float(input("Enter the principal amount ($): "))
rate = float(input("Enter the quoted interest rate (as a percentage, example: 5.5): "))
amortization = int(input("Enter the amortization period (in years): "))
    
    # Calculate payments
payments = mortgage_payments(principal, rate, amortization)
    
    # Output
print(f"Monthly Payment: ${payments[0]}")
print(f"Semi-monthly Payment: ${payments[1]}")
print(f"Bi-weekly Payment: ${payments[2]}")
print(f"Weekly Payment: ${payments[3]}")
print(f"Rapid Bi-weekly Payment: ${payments[4]}")
print(f"Rapid Weekly Payment: ${payments[5]}")
import math

loan_pri = int(input("Enter the loan principal: "))
print(loan_pri)
print("What do you want to calculate?")
print('Type "m" - for number of monthly payments,')
print('Type "p" - for the monthly payment:')
morp = str(input())
if morp == "m":
    print("Enter the monthly payment:")
    mp = int(input())
    res1 = loan_pri / mp
    res11 = round(res1)
    if res1 == 1:
      print("It will take " + str(res11) + " month to repay the loan")
    else:
      print("It will take " + str(res11) + " months to repay the loan")
else:
    print("Enter the number of months: ")
    nm = int(input())
    res2 = loan_pri / nm
    res22 = math.ceil(res2)
    lp = int(loan_pri - (nm -1) * res22)
    print("Your monthly payment = " + str(res22) + " and the last payment = " + str(lp))
    

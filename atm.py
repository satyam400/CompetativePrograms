x,bank_balance = [eval(x) for x in input().split()]
if x%5==0:
    if x+0.50<bank_balance:
        print(format(bank_balance-(x+0.50),".2f"))
    else:
        print(format(bank_balance,".2f"))
else:
    print(format(bank_balance,".2f"))

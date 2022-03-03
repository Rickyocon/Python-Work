iSalary = int(input("what is your salary?: "));
iCredit = int(input("what is your credit score?: "));
if iSalary>50000:
    if iCredit>800:
        print("Approved!");
    else:
        print("Denied");
else:
    print("Denied");

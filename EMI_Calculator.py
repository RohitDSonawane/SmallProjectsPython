#EMI calculator
print("Welcome to EMI Calculator")
Principal=int(input("Enter the Loan Amount: "))
time=int(input("enter the Loan tenure in years: "))
CIBIL=int(input("Enter the CIBIL Score: "))
rate=0
if CIBIL>=800:
  rate=7.5
else:
  rate=8.5

r = (rate / 100) / 12
n = time * 12

E=(Principal*r*((1+r)**n))/(((1+r)**n)-1)
T=E*time*12
Total_intrest=T-Principal
print(" ")
print("The Loan EMI is: ",E)
print("The Total Intrest payable: ",Total_intrest)
print("Principle Loan amount=",(Principal/T)*100,"Total Intrest=",(Total_intrest/T)*100)
print("The total Payment after",time,"years: ",T)
print(" ")
print("\nMonth-by-Month EMI Schedule:")
print("Month | EMI | Principal Paid | Interest Paid | Remaining Balance")

remaining_balance = Principal
for month in range(1, n + 1):
    interest_paid = remaining_balance * r
    principal_paid = E - interest_paid
    remaining_balance -= principal_paid
    print(f"{month:5} | {E:5.2f} | {principal_paid:15.2f} | {interest_paid:13.2f} | {remaining_balance:18.2f}")

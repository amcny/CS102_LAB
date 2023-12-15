salary=int(input("Enter Salary: "))
gender=input("Enter M for male and F for female: ")
bonus=0
if gender=='M':
    bonus=0.05*salary
else:
    bonus=0.1*salary
print("Bonus=",bonus)
print("Final Salary=",salary+bonus)
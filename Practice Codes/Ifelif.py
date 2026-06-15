print("-----------------------------------------------------")
print("------------- Ticket pricing Software ---------------")
print("-----------------------------------------------------")

print("Please Enter Your Age :")
age = int(input())

if(age <= 5):
    print(" Free ")
elif(age > 5 and age <= 18):
    print(" 900 ")
elif(age > 18 and age <= 40):
    print(" 1200 ")
else:
    print(" 500 ")

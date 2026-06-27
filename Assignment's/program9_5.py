# Q.5  Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15 
# Output: Divisible by 3 and 5

def Div(No):
    if No % 3 == 0 or No % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Number is Not Divisible by 3 and 5")

def main():
    Value = int(input("Enter Your Number : "))

    Div(Value)

if __name__ == "__main__":
    main()
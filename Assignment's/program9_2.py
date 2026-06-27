# Q.2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
# Input: 10 20 
# Output: 20 is greater

def ChkGreater(No1, No2):
    Ans = max(No1, No2)
    return Ans

def main():
    Value1 = int(input("Enter First Number  : "))
    Value2 = int(input("Enter Second Number : "))

    Ret = ChkGreater(Value1,Value2)

    print("Greater Number is : ",Ret)

if __name__ == "__main__":
    main()
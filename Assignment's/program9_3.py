# Q.3  Write a program which accepts one number and prints square of that number.
# Input: 5 
# Output: 25

def square(num):
    Ans = num * num
    return Ans

def main():
    NUM = int(input("Enter Your Number : "))

    Ret = square(NUM)

    print("Square is : ",Ret)

if __name__ == "__main__":
    main()
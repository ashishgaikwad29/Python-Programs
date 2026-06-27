# Q.4  Write a program which accepts one number and prints cube of that number

def cube(NUM):
    Ans = NUM * NUM * NUM
    return Ans

def main():
    Value = int(input("Enter Your Number : "))

    Ret = cube(Value)

    print("Cube is : ",Ret) 

if __name__ == "__main__":
    main()
#CIS 116 section 2095 22/FA
#Derek Johnson
#Aspis00
#September 29, 2022
#Assignment #4
#If statement checks and other practice.



#checking if user inputs are equal
Num1 = int(input("Enter an integer: "))
Num2 = int(input("Enter an integer: "))
if Num1 == Num2:
    print(f"{Num1} and {Num2} are equal.")
else:
    print(f"{Num1} and {Num2} are not equal.")

#check if number is even or odd (floats are NOT classified as even or odd, program will crash if fed a float type)
UserInput = int(input("Enter an INTEGER to see if its even or odd: "))
if UserInput % 2 == 0:
    print(f"{UserInput} is an even number.")
else:
    print(f"{UserInput} is an odd number.")

#check for positive or negative
Var1 = int(input("Enter a number to see if its positive or negative: "))
if Var1 < 0:
    print(f"{Var1} is a negative number.")
else:
    print(f"{Var1} is a positive number.")

#checking if a given year is a leap year
UserYear = int(input("Enter a year to see if it's a leap year: "))
if UserYear % 4 == 0:
    print(f"{UserYear} is a leap year.")
else:
    print(f"{UserYear} is not a leap year.")

#check voter age
VoterAge = int(input("Enter your age to verify eligibility to vote: "))
if VoterAge >= 18:
    print(f"Congratulations! You are able to cast your vote!")
elif VoterAge < 18 and VoterAge > 0:
    print(f"Sorry, you are not able to vote yet.")

#M value check
m = int(input("Enter a value: "))
if m >= 0:
    n = 1
elif m <0:
    n = -1
print(f"The value of n = {n}")

#checking height and organizing by height
height = int(input("Enter your height in centimeters: "))
if height < 180:
    print("You are short.")
elif height > 180:
    print("You are tall.")

#finding the largest number
int1 = int(input("Enter 3 numbers: "))
int2 = int(input())
int3 = int(input())
if int1 >= int2 and int1 >= int3:
    BiggestNumber = "first"
elif int2 >= int1 and int2 >= int3:
    BiggestNumber = "second"
else:
    BiggestNumber = "third"
print(f"First number: {int1}")
print(f"Second number: {int2}")
print(f"Third number: {int3}")
print(f"The {BiggestNumber} number is the greatest among the three.")

#pet match statement
UserPet = input("Do you have a fish, dog, cat or squirrel? Enter what pet you have: ")
if UserPet.upper() == "FISH":
    print("You own a fish.")
elif UserPet.upper() == "DOG":
    print("You own a dog.")
elif UserPet.upper() == "CAT":
    print("You own a cat.")
elif UserPet.upper() == "SQUIRREL":
    print("You have issues but you own a squirrel.")
else:
    print("You need a friend. :(")

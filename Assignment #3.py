#CIS 116 section 2095 22/FA
#Derek Johnson
#Aspis00(GitHub ID)
#Thursday, September 22nd, 2022
#Assignment#3
#A program written that uses user inputs to practice data types.


# Check for version Python 3+
import sys

if sys.version_info < (3, 0):
    sys.exit("Use Python 3.0+ for this program")

user = input("Enter Your Name: ")

# get gas types and costs from user
CostReg = float(input("Enter the cost of Regular gas: "))
CostMid = float(input("Enter the cost of Mid Grade gas: "))
CostPrem = float(input("Enter the cost of Premium gas: "))
TankGal = float(input("Enter the size of your gas tank in gallons: "))

#list of gas types for outputs
GasTypes = ["Regular", "Mid Grade", "Premium"]

# dictionary data type for gas
GasPriceDict = {
    "Regular": CostReg,
    "Mid Grade": CostMid,
    "Premium": CostPrem,
}

# list data type from user
ValueList = [input("Enter a value: "), input("Enter a value: "), input("Enter a value: "),
             input("Enter a value: "), input("Enter a value: "), input("Enter a value: ")]
ValueList.pop(2)

# Tuple data type (rainbow colors)
ColorOfRainbow = ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet")

#Boolean Value data type
BoolVal = input("Enter a T: ")
if BoolVal.upper() == "T":
    BoolVal1 = True
else:
    BoolVal2 = False

#Set data types for unionization in outputs
Set1 = {"Hello", "Hi", "Hola"}
Set2 = {"How", "What", "When", "Why"}
Set3 = Set1.union(Set1, Set2)

print(f"Good Morning {user.upper()}")
print(f"the cost to fill your gas tank with {GasTypes[0]} is {GasPriceDict['Regular'] * TankGal:.2f}")
print(f"the cost to fill your gas tank with {GasTypes[1]} is {GasPriceDict['Mid Grade'] * TankGal:.2f}")
print(f"the cost to fill your gas tank with {GasTypes[2]} is {GasPriceDict['Premium'] * TankGal:.2f}")
print(f"The union of 2 sets contains the value {Set3}")
print(f"The value in position 3 of the Tuple is {ColorOfRainbow[2]}")


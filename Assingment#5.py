#CIS 116 section 2095 22/FA
#Derek Johnson
#Aspis00
#October 6, 2022
#Assignment #5
#Loops practice.

#Using a single character at a time create loops to  Print the following patterns:
#Pattern 1:
#*
#**
#***
#****
#Pattern 2
#  *
# ***
#*****
# ***
#  *

#Pattern 3
#1010101
# 10101
#  101
#   1
#Create a tuple that contains the following values and use a loop display the values.
#car
#boat
#fish
#cat
#floss
#toothbruch
#Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

#Pattern 1
for x in range(5):
    print("*" * x)

#Pattern 2
padding = (4,2,0,2,4)
max_stars = 5
for i in padding:
    print(int(i/2) * " " + "*" * (max_stars-i)) #could do floor division (i//2) to return int.

#Pattern 3
padding = 0
max_ones = 4
max_zeros = 3
for i in range(4):
    # define a set of zeros
    my_zeros = ["0"] * (max_zeros - i)
    for y in range(0,(max_ones-i)):
        my_zeros.insert(y*2, "1")
    # join them up
    my_zeros = ''.join(my_zeros)
    my_output = padding * " " + my_zeros
    padding += 1
    print(my_output)

#Create a tuple that contains the following values and use a loop display the values.
ItemTuple = ("car", "boat", "fish", "cat", "floss", "toothbrush")
for j in ItemTuple:
    print(j)

#Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.
UserInput1 = print("Enter as many integers as you would like to find the average of all of them. Press q to quit.")
UserInput = ""
listnum = []

while UserInput.upper() != "Q":
    UserInput = input("Enter an integer or q to quit: ")
    if not UserInput.isalpha():
        listnum.append(int(UserInput))
        print("The avererage is:", sum(listnum) // len(listnum))
        print("The sum is:", sum(listnum))
    elif UserInput.upper() == "Q":
        print("The avererage is:", sum(listnum) // len(listnum))
        print("The sum is:", sum(listnum))
    else:
        print("Try again")

print("Goodbye")




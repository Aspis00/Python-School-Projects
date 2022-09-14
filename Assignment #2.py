#CIS 116 Section 2095 22/FA
#Aspis00
#Sept. 13, 2022
#Assignment #2
#Mathmatic Equations Practice

Name = input("Enter Your Name: ")
print("Hello", Name)

#Decision = input("What can I help you with today? Enter: triangle, circle or age of my dog: ")

while True:
    Decision = (input("What can I help you with today? Enter: triangle, circle or age of my dog: "))
    if Decision == "triangle":
        break
    if Decision == "circle":
        break
    if Decision == "age of my dog":
        break
    else:
        print ("Check your spelling or enter one of the options.")

if Decision == ("triangle"):
    print("Enter the Base and Height")
    AT = float(input("Base: "))
    HT = float(input("Height: "))
    areaT = (float(round(AT * HT / 2, 2)))
    print("The area of that triangle is", areaT)

if Decision == ("circle"):
    print("Enter the radius of the circle: ")
    RC = float(input("Radius: "))
    DC = float(round(RC * 2, 2))
    print("The diameter of that circle is", DC)

if Decision == ("age of my dog"):
    DN = input("Enter your dogs name: ")
    print("Enter",DN + "'s", "age in human years")
    HY = float(input("Age: "))
    DY = float(round(HY * 7, 2))
    print("The age of your good dog", DN, "is", DY, ":)")

print("Have a wonderful day.")

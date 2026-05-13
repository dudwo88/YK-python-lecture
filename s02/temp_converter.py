"""
Author: Youngjae Kim
Date: 2026-05-08
Description: 
    Use input() to receive a Celsius temperature, 
    convert it to Fahrenheit (F = C x 9/5 + 32), and print the result clearly
"""
# Very simple logic
# ctemp = float(input("Enter temperature in Celsius: "))
# ftemp = ctemp * 9/5 + 32
# print(f"{ctemp:.1f}°C = {ftemp:.1f}°F")


# Enahced one - with error checking.
# Need more (what if the input value is not number type)
ctempstr = input("Enter temperature in Celsius: ");
if ctempstr.isdigit(): #=> This is more recommended.
    ftemp = float(ctempstr) * 9/5 + 32
    print(f"{float(ctempstr):.1f}°C = {ftemp:.1f}°F")
else:
    print("Please enter only digit number.")

## more enhanced -> if the input value is wrong => asking again. (after learn while)


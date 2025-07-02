# Given three points (x1, y1), (x2, y2), (x3, y3),
# write a program to check all the three points fall on one straight line.
x1=int(input("Enter the x1 point:"))
x2=int(input("Enter the x2 point:"))
x3=int(input("Enter the x3 point:"))
y1=int(input("Enter the y1 point:"))
y2=int(input("Enter the y2 point:"))
y3=int(input("Enter the y3 point:"))

def straight_line(x1, y1, x2, y2, x3, y3):
    
    return  x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

if straight_line(x1, y1, x2, y2, x3, y3):
    print("The points are straight_line.")
else:
    print("The points are not straight_line.")

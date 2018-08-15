#Calculate the area of a sector
pi = 3.142
theta = 20
r = 6
# Ask for pi
pi = float(input("What is pi:\n"))
# Ask for theta
theta = int(input("What is theta:\n"))
#Ask for r
r = int(input("What is radius:\n"))
# Ask for area
area = (theta/2*pi) * pi*r**2
print(area)
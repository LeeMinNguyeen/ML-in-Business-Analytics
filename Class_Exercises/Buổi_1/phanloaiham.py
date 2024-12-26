'''
    Name: Le Minh Nguyenn
    Student ID: K224161829
'''

### Fuction ###
def printData(x):
    print(x)
    
def average(a,b,c):
    return (a+b+c)/3

printData(980)

x = printData(800)
print("x=", x) # None

t = average(1,4,7)
print("t=", t)

def double(n):
    return n*2

### Documentation for the function ###
def firstDegree(a, b):
    """
    Solve the first-degree equation ax + b = 0.

        a (float): Coefficient a.
        b (float): Coefficient b.

    Returns:
        None: Prints the solution to the equation.
        - If a == 0 and b == 0, prints "Phuong trinh vo so nghiem" (The equation has infinitely many solutions).
        - If a == 0 and b != 0, prints "Phuong trinh vo nghiem" (The equation has no solution).
        - Otherwise, prints "Phuong trinh co nghiem x = " followed by the solution x = -b/a.
    """
    if a == 0 and b == 0:
        print("Phuong trinh vo so nghiem")
    elif a == 0 and b != 0:
        print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem x = ", -b/a)

print("Phuong trinh bac 1")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
firstDegree(a, b)

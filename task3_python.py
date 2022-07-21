from math import sqrt

def find_roots(a,b,c):
    b2 = (b**2)-(4*a*c)
    b2 = sqrt(b2)
    a=2*a
    return ((-b + b2)/(a),(-b - b2)/(a))



if __name__ == '__main__':
    x1,x2 = find_roots(2,10,8)
    print(f"The root of the equations are {x1} and {x2} ")
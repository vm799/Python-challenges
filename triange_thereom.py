# a triangle is valid if sum of its two sides is greater than the third side

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True

    else:
        return False
    
    
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
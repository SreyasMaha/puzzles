import math

def score(x, y):
    p = math.sqrt(x**2 + y**2)
    out = 10
    if p > 1:
        out = out - 5
    
    if p > 5:
        out = out - 4
    
    if p > 10:
        out = out - 1

    return out 
    

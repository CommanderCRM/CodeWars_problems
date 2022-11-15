def is_square(n):    
    import math
    if n >= 0:
        root = math.sqrt(n)
        if root*root == n:
            return True
        elif n < 0:
            return False
        else:
            return False
    else:
        return False

def is_square(n):    
    import math
    if n >= 0:
        root = math.sqrt(n)
        if root*root == n:
            return True
        else:
            return False
    else:
        return False

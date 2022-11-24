def rgb(r, g, b):
    return "{0:02X}{1:02X}{2:02X}".format(clamp(r), clamp(g), clamp(b))

def clamp(x): 
    return max(0, min(x, 255))

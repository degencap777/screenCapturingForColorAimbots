import math
def checksum(p):
    o = (24 * 500 * 3) + (500//2) * 3 - 13 * 3
    if not(p[o] == 0 and p[o+1] == 255 and p[o+2] == 0):
        return None
    t = None
    lm = None
    b = -1
    for xx, yy in enumerate(range(0, len(p), 3)):
        v = p[yy]
        w = p[yy+1]
        h = p[yy+2]
        j, i = divmod(xx, 500)
        if abs(v-w) < 2 and v > 0x87 and h < 15:
            if t is None:
                lm = i
                t = j
            b = j
    if t is None:
        return None                    
    f = 0xf0
    dx = lm-500//2
    dy = math.ceil((b-t)/7)+t-50//2
    if abs(dx) > 10:
        m = 0.5
    else:
        m = 1
    return f, round(m*dx), round(m*dy)

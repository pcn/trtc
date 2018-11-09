

def eq(t1, t2, epsilon=.000001):
    """Tests for equality of two numbers, with a fudge factor for when
    gotta be floats"""
    if abs(t1 - t2) < epsilon:
        return True
    else:
        return False
    

def normalize(min_val, max_val, float_val):
    """Normalize a floating point value between 0 and 1, floating point,
    between min and max."""
    therange = abs(max_val - min_val)
    

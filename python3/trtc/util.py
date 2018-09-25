

def eq(t1, t2, epsilon=.000001):
    """Tests for equality of two numbers, with a fudge factor for when
    gotta be floats"""
    if abs(t1 - t2) < epsilon:
        return True
    else:
        return False
    
    

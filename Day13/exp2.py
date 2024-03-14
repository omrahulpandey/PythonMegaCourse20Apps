def calculate_time(h, g=9.80665 ):
    """Calculate time for free fall of object and return it."""
    t = (2 * h / g) ** 0.5
    return t
    
  
time = calculate_time(100)
print(time)
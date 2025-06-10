def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    min_max = f"Max: {maximum}\nMin: {minimum}"
    return min_max
    
print(get_max())
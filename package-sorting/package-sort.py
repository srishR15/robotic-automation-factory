def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in (width, height, length))
    is_heavy = mass >= 20
    
    return "REJECTED" if is_bulky and is_heavy else "SPECIAL" if is_bulky or is_heavy else "STANDARD"


print(sort(100, 100, 100, 10))  # SPECIAL (not bulky, not heavy)
print(sort(200, 50, 10, 15))    # SPECIAL (bulky but not heavy)
print(sort(100, 100, 50, 25))   # SPECIAL (heavy but not bulky)
print(sort(200, 200, 200, 30))  # REJECTED (both bulky and heavy)
print(sort(100,50,20,10))       # STANDARD (not bulky, not heavy)
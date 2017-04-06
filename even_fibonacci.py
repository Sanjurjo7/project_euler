total = 2
a, b = 1,2

while b <= 4000000:
    c = a + b
    a = b
    b = c
    if not c%2:
        total += c

print(total)
    

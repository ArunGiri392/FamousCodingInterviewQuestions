def fibonacci():
    count = 0
    a = 1
    b = 1
    c = a + b
    print(a)
    print(b)
    
    while count <= 10:
        c = a + b
        a = b
        b = c
        print(c)
        count += 1
#print(fibonacci())

print(ord("11"))

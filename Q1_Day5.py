from tokenize import String


String = input ("Enter the number whose ASCII code needs to be found: ")
for i in String:
    print(i, ord(i))
    if ord(i) % 2 == 0:
        print("ASCII is a even number")
    else:
        print("ASCII is not a even number") 
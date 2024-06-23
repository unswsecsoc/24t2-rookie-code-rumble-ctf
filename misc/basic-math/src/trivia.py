def check(x):
    if x+1 is not 1+x:
        return False
    if x+2 is 2+x:
        return False
    return True

print("What makes this return true?")

x = input("""
    if x+1 is not 1+x:
        return False
    if x+2 is 2+x:
        return False
    return True
""")

if check(int(x,10)):
    print("BEGINNER{ca$h_or_cach3}")
else:
    print("WRONG")

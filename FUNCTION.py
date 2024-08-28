TOTAL=0
def sum (a,b=0):
    print("a",a)
    print("b",b)
    TOTAL = a + b
    print("TOTAL inside function:",TOTAL)
    return TOTAL
n=sum(4,6)
TOTAL = TOTAL
print("TOTAL outside function:",TOTAL)
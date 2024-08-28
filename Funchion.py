total=0
def sum(a,b=0):
     print ("a:",a)
     print ("b:",b)

     total=a+b
     print ("total inside function: ",total)

     return total


n = sum(5,6)

    print ("Total outside function :",total )

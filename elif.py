Bangladeshi = [" fuska", " rice", "berani", ]
Pakistani = [" kabab", "basmati", "chap"]
indian =[ " kari", "razma rice", "misty"]
dish = input("Emter the dish name :")
if dish in Bangladeshi:
    print("Bangladeshi")
elif dish in Pakistani:
    print("Pakistani")
elif dish in indian :
    print("Indian")
else:
    print("no country", dish)
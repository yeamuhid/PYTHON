key_locattion = "chair"
location= [ "chair","grage","store room"]
for i in location:
    if i ==key_locattion:
        print("key is found in", i)
        break
    else:
        print("key is not found in ",i)
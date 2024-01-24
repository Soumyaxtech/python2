d = {"tom":123,"joe":567,"max":900}
print(d["tom"])
d["jenny"]= 345 # ADD ITEM IN DICTIONARY
print(d) # to print dictionary
del d["max"]  # IT DELETE ITEM FROM DICTIONARY
print(d)
for key in d:
    print(key,":",d[key])
print("tom" in d)   # TO CHECK IF THIS ITEM IS IN DICTIONARY OR NOT
d.clear()  # TO EMPTY THE DICTIONARY
print(d)
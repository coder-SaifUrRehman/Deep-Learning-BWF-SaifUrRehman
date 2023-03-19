guests = ['Shafiq', 'Ali', 'Saifi']
not_coming = guests.pop(1) 

print(f"sry, {not_coming},you cannot come to the the dinner.")

new = "Haseeb"
guests.insert(1,new) 
for i in guests:
    print(f"{i} You will come for dinner")
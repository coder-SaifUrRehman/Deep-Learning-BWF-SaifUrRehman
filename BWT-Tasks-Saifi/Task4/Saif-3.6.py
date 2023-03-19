guests = ['Shafiq', 'Ali', 'Saifi']
not_coming = guests.pop(1) 
print(f"Unfortunately, {not_coming} cannot come to the the dinner.")


new = ['Atif', 'Ahmed', 'Baber']
middle = int(len(guests)/2)
guests.insert(0, new[0])  
guests.insert(middle,new[1]) 
guests.append(str(new[2:]))  

for i in guests:
    print(f"Hey! {i} Come for dinner")




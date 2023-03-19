res_menu = ('biryani', 'chicken','sandwich', 'pizza', 'coca-cola')

print("Menu:")
for i in res_menu:
    print("\t",i)

#res_menu[0] = "beef"
# raise an error as tuples are immutable....


res_new_menu = ('biryani', 'chicken','mutton', 'beef', 'coca-cola')

print("New menu:")
for i in res_new_menu:
    print("\t",i)


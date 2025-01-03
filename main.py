my_list = [0]
if len(my_list) <=1:
    my_list.insert(0, my_list.pop(-1))
print(my_list)
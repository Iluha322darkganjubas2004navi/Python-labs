def list_of_evens(my_list, temp_list):
    for i in my_list:
        if i % 2 == 0:
            temp_list.append(i)
    return temp_list
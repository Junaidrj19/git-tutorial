def gimme(input_array):
    my_list = input_array
    max1 = max(my_list)
    min1 = min(my_list)

    for number,i in enumerate(my_list):
        if max1 > number > min1:
            return i

print(gimme([2,3,1]))

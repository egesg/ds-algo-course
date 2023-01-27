# there are also indexes here different than bubble sort.
# we keep track of index where the min value is -> start with min_index = 0

# my_list = [4, 2, 6, 5, 1, 3]
# indexes    0  1  2  3  4  5

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index: # if i and min_index are equal, do not run these codes because no need to swap values
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list
   
original_list = [4, 2, 6, 5, 1, 3]
sorted_list = selection_sort(original_list)
print((original_list)) # in place sort, original list did not stay same. 
# [1, 2, 3, 4, 5, 6]
print(selection_sort(original_list))
# [1, 2, 3, 4, 5, 6]

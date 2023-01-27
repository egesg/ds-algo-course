# my_list = [4, 2, 6, 5, 1, 3]

# always start with the second item in the list
# compare it with the item before it
# move it over until it is compared with the item which is not less than (while loop)

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1: # j has to be greater than -1 so it does not break me out of the while loop
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

original_list = [4, 2, 6, 5, 1, 3]
sorted_list = insertion_sort(original_list)
print((original_list)) # in place sort, original list did not stay same. 
# [1, 2, 3, 4, 5, 6]
print(insertion_sort(original_list))
# [1, 2, 3, 4, 5, 6]


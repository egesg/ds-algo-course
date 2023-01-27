def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index 

    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort(my_list, left, right): # runs pivot helper function recursively on the right side and left side
    if left < right:
        pivot_index = pivot(my_list, left, right) # pivot helper function returned to index 3 which is value of 4
        quick_sort(my_list, left, pivot_index - 1) # call the function recursively on the left side
        quick_sort(my_list, pivot_index + 1, right) # call the function recursively on the right side
    return my_list

my_list = [4, 6, 1, 7, 3, 2, 5]
quick_sort = quick_sort(my_list, 0, 6)
print(quick_sort)
# [1, 2, 3, 4, 5, 6, 7]
print(my_list)
# [1, 2, 3, 4, 5, 6, 7]


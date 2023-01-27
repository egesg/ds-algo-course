# 4 6 1 7 3 2 5

def swap(my_list, index1, index2): # this will be called 2 times so I created a function
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# pivot_index = 0
# end_index = 6 -> (len(my_list) - 1)
def pivot(my_list, pivot_index, end_index): # 1- rearranges the item in the list so they look like this ( 2 1 3 - 4 - 6 7 5 ) 2-returns to swap_index
    swap_index = pivot_index 

    for i in range(pivot_index+1, end_index+1): # after for loop done -> list will look like this end of the loop -> 4 - 1 3 2 - 6 7 5
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1 # 1st thing to do -> swap_index + 1
            swap(my_list, swap_index, i) # 2nd thign to do -> swap the items at i and at swap_index
    
    swap(my_list, pivot_index, swap_index) # swaps the pivot index (value of 4) and swap_index (value of 2) ->  once this line done -> list will look like this -> 2 1 3 - 4 - 6 7 5
                                           # everything less than 4 stays on the left side and everthing greaster than 4 stays on the right side
    return swap_index # returns to the index 3 not value of 4

my_list = [4, 6, 1, 7, 3, 2, 5]
pivot_list = pivot(my_list, 0, 6)
print(pivot_list)
# 3
print(my_list)
# [2, 1, 3, 4, 6, 7, 5] -> 4 is in the middle. all the items that is less than 4 are on the left side, all the item that is greater than 4 are on the right side.


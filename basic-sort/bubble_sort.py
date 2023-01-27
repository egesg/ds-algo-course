# start from the beginning

# my_list = [4, 2, 6, 5, 1, 3]
#            2, 4, 5, 1, 3, 6 -> we did 5 comparisons for 6 items -> 6 -> sorted items will be bubbled up 
#            2, 4, 1, 3, 5    ->        4 comparisons for 5 items -> 5, 6 -> these two are sorted now
#            2, 1, 3, 4       ->        3 comparisons for 4 items -> 4, 5, 6
#            1, 2, 3          ->        2 comparisons for 3 items -> 3, 4, 5, 6

def bubble_sort(my_list):
    # range(len(my_list) - 1) -> 6 - 1 = 5 -> 5 comparisons
    # range(5,0,-1)
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i): # j will run 5 times -> will do 5 comparisons 
            if my_list[j] > my_list[j+1]: # if 4 > 2 -> switch these 2
                temp = my_list[j] # temp = 4
                my_list[j] = my_list[j+1] # will move value 2 to place of value 4
                my_list[j+1] = temp # value 4 will move to place of value 2
    return my_list

original_list = [4, 2, 6, 5, 1, 3]
sorted_list = bubble_sort(original_list)
print((original_list)) # in place sort, original list did not stay same. 
# [1, 2, 3, 4, 5, 6]
print(bubble_sort(original_list))
# [1, 2, 3, 4, 5, 6]
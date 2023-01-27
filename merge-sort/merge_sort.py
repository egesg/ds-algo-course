# 1- write the code that breaks the list in half (use recursion)
# 2- base case -> when len(the_list) is 1
# 3- use merge() helper function to put the lists together

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list # once the return is called, my_list popped off from the call stack

    mid_index = int(len(my_list)/2) # if len of the list is odd
    left = merge_sort(my_list[:mid_index]) # it is up to mid_index but not included - merge_sort() breaks the list until it has 1 item in it (1 item list counts as sorted by definition, so I can pass it to merge helper function)
    right = merge_sort(my_list[mid_index:])

    return merge(left, right) # merge function only works on sorted lists

original_list = [3,1,4,2]
sorted_list = merge_sort(original_list)
print('Original List:',original_list) # original list stayed same 
# Original List: [3, 1, 4, 2]
print('Sorted List:',sorted_list) 
# Sorted List: [1, 2, 3, 4]

# other sorting algorithms (bubble sort, insertion, selection) sort the list in place. so original list will be sorted when we are done.
# but in merge sort, the original list stays the same and it returns a seperate sorted list.

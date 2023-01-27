# 1 3 7 8  -  2 4 5 6   -> 2 sorted lists
#    1 2 3 4 5 6   7 8  -> keep sorting until one of the list has no item left

# helper function
def merge(list1, list2):
    combined = []
    i = 0 # index of 0 in list1
    j = 0 # index of 0 in list2
    while i < len(list1) and j < len(list2): # as long as both lists still have items in them, keep running this
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

print(merge([1,2,7,8],[3,4,5,6]))
# [1, 2, 3, 4, 5, 6, 7, 8]

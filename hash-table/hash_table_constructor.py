class HashTable:
    # constructor
    def __init__(self, size=7) -> None: # default size / have always prime number of address (prime number reduces collisions because it increases the amount of randomness for how key value pairs are going to be distributed thought the hash table)
        self.data_map = [None] * size # create a list with 7 items in it and all of those are going to contain None.

    def __hash(self,key) -> int:
        my_hash = 0
        for letter in key:
            # ord(letter) - ordinal -> gets the ASCII number for each letter as we loop thorugh it
            # 23 -> I can plug any prime number in here
            # len(self.data_map) -> 7
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # so remainder will be anywhere from 0 to 6 -> this is my address space
        return my_hash # return to the address from 0 to 6

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

my_hash_table = HashTable()

my_hash_table.print_table()
# 0 :  None
# 1 :  None
# 2 :  None
# 3 :  None
# 4 :  None
# 5 :  None
# 6 :  None


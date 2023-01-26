class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self,key) -> int:
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    
    def set_method(self,key,value):
        index = self.__hash(key) # address to store key value pair
        if self.data_map[index] == None: # if there is nothing in that address yet
            self.data_map[index] = [] # initialize the empty list at that address
        self.data_map[index].append([key, value]) # if there is alreay item, just append

my_hash_table = HashTable()
my_hash_table.print_table()
# 0 :  None
# 1 :  None
# 2 :  None
# 3 :  None
# 4 :  None
# 5 :  None
# 6 :  None
my_hash_table.set_method('bolts', 1400)
my_hash_table.set_method('washers', 50)
my_hash_table.set_method('lumber', 70)
my_hash_table.print_table()
# 0 :  None
# 1 :  None
# 2 :  None
# 3 :  None
# 4 :  [['bolts', 1400], ['washers', 50]]
# 5 :  None
# 6 :  [['lumber', 70]]


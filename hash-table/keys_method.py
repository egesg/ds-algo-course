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
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_method(self,key):
        index = self.__hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)): # loop through data_map list
            if self.data_map[i] is not None: # if there is a list inside of the data_map list
                for j in range(len(self.data_map[i])): # loop through that list
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable()
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
print(my_hash_table.keys())
# ['bolts', 'washers', 'lumber']


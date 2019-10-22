class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = (2 ** (depth + 1)) - 1
        self.Tree = [None] * self.tree_size # массив ключей
    
    def FindKeyIndex(self, key):
        current_index = 0
        # ищем в массиве индекс ключа
        while current_index < self.tree_size:
            if self.Tree[current_index] is None:
                return -current_index
            if self.Tree[current_index] == key:
                return current_index
            elif self.Tree[current_index] < key :
                current_index = current_index * 2 + 2
                if current_index not in range(self.tree_size):
                    return None
            elif self.Tree[current_index] > key :
                current_index *= 2 + 1
                if current_index not in range(self.tree_size):
                    return None
        return None # не найден
    
    def AddKey(self, key):
        result_index = self.FindKeyIndex(key)
        if result_index == 0:
            self.Tree[0] = key
            return 0
        if result_index is None:
            return -1
        if result_index < 0:
            self.Tree[-result_index] = key
            return -result_index
        if result_index >= 0:
            return -1
        # добавляем ключ в массив
        # индекс добавленного/существующего ключа или -1 если не удалось
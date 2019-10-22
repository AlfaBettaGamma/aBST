class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2 ** (depth + 1) - 1
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
            elif self.Tree[current_index] > key :
                current_index = current_index * 2 + 1
        return None # не найден
    
    def AddKey(self, key):
        result_index = self.FindKeyIndex(key)
        if result_index is not None:
            result_index = abs(result_index)
            self.Tree[result_index] = key
            return result_index
        else:
            return -1
        # добавляем ключ в массив
        # индекс добавленного/существующего ключа или -1 если не удалось
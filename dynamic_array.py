# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Brook Hamilton
import numpy as np

class DynamicArray:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.data = np.ndarray(self.capacity, dtype = object)
        
    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size

    def append(self, num):
        self.data[self.size] = num
        self.size += 1

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Out of bounds")
        return self.data[index]

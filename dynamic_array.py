# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Brook Hamilton
import numpy as np

class DynamicArray:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.next_index = 0
        self.data = np.ndarray(self.capacity, dtype = object)
        
    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size

    def append(self, num):
        if self.size == len(self.data):
            self.resize()
        self.data[self.size] = num
        self.size += 1
        self.next_index += 1

            
    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range.")
        return self.data[index]
    
    def clear(self):
        self.size = 0
        self.next_index = 0

    def pop(self):
        if self.size == 0:
            raise IndexError("Empty data structure")
        last_element = self.data[self.size - 1]
        self.size -= 1
        return last_element
    
    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range.")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    def insert(self, index, num):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == len(self.data):
            self.resize()
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = num
        self.size += 1

    def is_full(self):
        if self.size == len(self.data):
            return True
        else:
            return False
        
    def resize(self):
        self.capacity *= 2
        new_arr = np.ndarray(self.capacity, dtype = object)
        for i in range(self.size):
            new_arr[i] = self.data[i]
        self.data = new_arr

    def max(self):
        largest_value = self.data[0]
        for i in range(self.size):
            if self.data[i] > largest_value:
                largest_value = self.data[i]
        return largest_value
    
    def min(self):
        smallest_value = self.data[0]
        for i in range(self.size):
            if self.data[i] < smallest_value:
                smallest_value = self.data[i]
        return smallest_value
            
    def sum(self):
        if self.size == 0:
            sum = None
        else:
            sum = 0
        for i in range(self.size):
            sum = sum + self.data[i]
        return sum

    def linear_search(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return None
    
    def binary_search(self, value):
        low = 0
        high = len(self) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.data[mid] == value:
                return mid
            elif self.data[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return None

# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Brook Hamilton

class DynamicArray:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr = [None] * capacity
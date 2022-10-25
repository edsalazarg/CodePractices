# First try

import random
import time

class SelectSort:

    def __init__(self, arr):
        self.arr = arr
        self.time = time.time()
        self.final_result = self.select_sort()
        print(f"--- {time.time() - self.time} seconds ---")
        
    
    def select_sort(self):
        i = 0
        x = 0
        while x < self.arr.__len__():
            min_idx = x
            i = x
            while i < self.arr.__len__():
                if self.arr[i] < self.arr[min_idx]:
                    self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
                i += 1
            x += 1
        return self.arr

objSelect = SelectSort(random.sample(range(0, 10000), 1000))
print(objSelect.final_result)
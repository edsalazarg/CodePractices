import random
import time


class BubbleSort:
    
    def __init__(self, arr):
        self.arr  = arr
        self.current_time = time.time()
        self.final_result = self.sort_algorithm()
        print(f" {time.time() - self.current_time} seconds")

    def sort_algorithm(self):
        swapped = False
        for _ in range(len(self.arr)):
            for i in range(len(self.arr) - 1):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True
            if not swapped:
                break
        return self.arr

objBs = BubbleSort(random.sample(range(0, 10), 5))
print(objBs.final_result)
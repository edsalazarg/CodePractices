import random
import time


class InsertSort:
    
    def __init__(self, arr):
        self.arr  = arr
        self.current_time = time.time()
        self.final_result = self.sort_algorithm()
        print(f" {time.time() - self.current_time} seconds")
    
    def __swap(self, idx1, idx2):
        self.arr[idx1] , self.arr[idx2] = self.arr[idx2], self.arr[idx1]

    def sort_algorithm(self):
        for x in range(self.arr.__len__()):
            i = x
            while self.arr[i] < self.arr[i -1] and i > 0:
                self.__swap(i, i-1)
                i -= 1
        return self.arr

objIS = InsertSort(random.sample(range(0, 10000), 1000))
print(objIS.final_result)
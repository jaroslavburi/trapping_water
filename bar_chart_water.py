#!/usr/bin/python
class bar_chart_water:

    water_amount = 0
    array = None
    
    def walk_array(self, idx, max):

        if self.array[idx] > max:
            max = self.array[idx]
        else: #drop
            self.water_amount += max - self.array[idx]

        return idx, max

    def run(self):
        left_idx = 0
        right_idx = len(self.array) -1;

        left_max = 0
        right_max = 0

        while left_idx <= right_idx:

            if (left_max <= right_max):
                left_idx, left_max = self.walk_array(left_idx, left_max)
                left_idx+=1

            else: #go from right
                right_idx, right_max = self.walk_array(right_idx, right_max)
                right_idx-=1

        return self.water_amount

    def __init__(self, array):
        self.array = array
        
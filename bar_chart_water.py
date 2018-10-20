#!/usr/bin/python

def bar_chart_water(array):
    #helper variables
    max = 0
    max_pos = -1
    second_highest = 0
    second_highest_pos = 0

    last_element_idx = len(array) -1;

    water_amount = 0
    for idx, bar in enumerate(array):
        if bar >= max:
            max = bar
            max_pos = idx
            second_highest = 0
            second_highest_pos = 0

        else: #drop -> start counting
            water_amount += max - bar

            if bar >= second_highest:
                second_highest = bar
                second_highest_pos = idx

            #last element and we didnt find same high border - need to substract missing water
            if idx == last_element_idx:
                width = last_element_idx - max_pos
                height = max - second_highest
                water_amount -= width * height

                #remove water on the far side without border
                width = last_element_idx - second_highest_pos
                height = max - second_highest
                water_amount -= width * height

    return water_amount

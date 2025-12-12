# Dam Breaking Problem
import sys
import heapq

def dam_breaking(n, threshold, drain, cracks):

    total_num_cracks = n
    time = 0
    existing_cracks = []
    max_level = 0
    remaining_water = 0
    solved = 0

    while total_num_cracks > 0:
        # first, add cracks appearing at this time unit
        if time in cracks:
            for item in cracks[time]:
                existing_cracks.append(item) # add cracks to existing cracks list
            heapq.heapify(existing_cracks) # convert to max-heap. Value stored as negative for max-heap
        
        if existing_cracks:
            heapq.heappop(existing_cracks) # fix largest crack
            solved += 1
        else:
            time += 1
            remaining_water = max(0, remaining_water - drain) # drain water if no cracks
            continue

        # then, calculate incoming water level
        incoming_water = -sum(existing_cracks) # sum of existing cracks (convert back to positive)
        remaining_water = max(0, remaining_water + incoming_water - drain)

        # check for max water level
        if remaining_water > max_level:
            max_level = remaining_water

        if remaining_water >= threshold: # if flood occurs, print and return
            print('FLOOD')
            print(time)
            print(remaining_water)
            return
        else: # if no flood
            if time < max(cracks.keys()): # if there are future cracks
                if existing_cracks: # if there are existing cracks
                # update existing cracks for next time unit
                    existing_cracks = [level - 1 for level in existing_cracks] # cracks widen by 1 unit (decrease negative value by 1)
                    time += 1
                    total_num_cracks = n - solved
                    continue
                else: # if no existing cracks but future cracks exist
                    time += 1
                    total_num_cracks = n - solved
                    continue
            else: # if no future cracks will appear from now on
                if len(existing_cracks) <= 1: # if 0 or 1 existing cracks, end the algorithm
                    print('SAFE')
                    print(max_level)
                    return
                elif len(existing_cracks) > 1: # if more than 1 existing cracks
                    # update existing cracks for next time unit
                    existing_cracks = [level - 1 for level in existing_cracks] # cracks widen by 1 unit (decrease negative value by 1)
                    time += 1
                    total_num_cracks = n - solved
                    continue



def main():
    # standard input reading
    input_data = sys.stdin.read().strip().splitlines()

    n = int(input_data[0]) # first line: number of cracks across all time units
    threshold = int(input_data[1]) # second line: water level threshold
    drain = int(input_data[2]) # third line: water drained per time unit

    # subsequent lines: read into a dictionary with time units as keys and lists of water levels as values
    cracks = {}
    
    for line in input_data[3:]:
        time_unit, water_level = line.split()
        time_unit = int(time_unit)
        water_level = int(water_level)
        if time_unit not in cracks:
            cracks[time_unit] = []
        cracks[time_unit].append(-water_level) # store negative for max-heap in the function

    # print('Cracks data:', cracks)
    dam_breaking(n, threshold, drain, cracks)




if __name__ == "__main__":
    main()



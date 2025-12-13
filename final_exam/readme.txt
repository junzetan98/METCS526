Question 1: 
    Input: 
        python question1_edit.py < flood_1 ~ 12.txt
    Output: 
        Screenshot Question_1 flood_Input 1-5.png
        Screenshot Question_1 flood_Input 6-10.png
        Screenshot Question_1 flood_Input 11-12.png
    Explanations:
        The core of the algorithm is to find and delete (pop) the largest crack while at the same time record
        the largest remaining water level at each time unit. The algorithm stops either when the remaining water
        level exceeds the threshold (causing flooding in the village) or when there is only 1 crack 
        remaining and no flooding occurs after water draining at a certain time unit (because at the beginning
        of the next time unit, the crack will be fixed and the remaining water level will never increase after 
        that). In other words, the algorithm will keep running when there are still cracks (either current cracks
        or cracks that will appear in the future) remaining.

        The rule of the algorithm is: at time x, if cracks appear, add those cracks to a 'to-be-fixed cracks' list.
        Then, immediately fix the largest crack among all the existing cracks. After that, water will come in from
        unfixed cracks, which will be followed by water draining by the village. After certain amount of water
        being drained, the remaining water level will be compared with the threshold. If remaining water exceeds
        the threshold, flooding occurs; if remaining water does not exceed the threshold, all the remaining cracks
        will be enlarged in size by 1 unit. The remaining water level will be kept for the next time unit. Then,
        if there will be cracks appearing in future time units, the algorithm keeps running and repeating the process
        (i.e. add new cracks, fix the largest crack if there are cracks left, add incoming water to the remaining water,
        and drain water to compare with the threshold) until there is flooding or only 1 crack left without flooding.

        To implement this algorithm, a max-heap is used to store the existing cracks that will appear at each
        time unit. The time unit values (e.g. 0 for time 0 and 5 for time 5) will be stored as keys in the 
        cracks dictionary, and the corresponding cracks will be stored as values for those keys. To repeat the 
        threshold comparison process, a while loop is used (while total number of cracks > 0), and starting from
        time = 0, check the cracks dictionary to see if there are any cracks that appear at this time. If yes, 
        push those cracks to the max-heap, so that the largest crack is always at the top of the heap (like a 
        priority queue where the largest value lines first). Then, immediately pop the first element in the 
        heap (meaning fixing the largest crack), and then calculate incoming water and remaining water. If there 
        is no existing crack, no incoming water will come, so we only need to drain water from remaining water,
        until the remaining water reaches 0 (we cannot drain water if there is no water to be drained). After 
        water draining, as stated before, we will compare the remaining water level with the threshold: if there 
        is flooding, print FLOOD and the time and remaining water level and end the algorithm; if there is no 
        flooding, check current time and maximum time in the cracks dictionary. If maximum time is not reached, continue
        the algorithm; if maximum time is reached (meaning no new cracks will appear), continue until there is 
        1 crack left, and if 1 crack is left without flooding, print SAFE and the maximum remaining water level (
        the largest remaining water level will be recorded and updated in each iteration.)


Question 2:
    Input:
        python question2_edit.py < ski_input1~3.txt
    Output: 
        Screenshot Question_2 ski_input 1-3.png
    Explanations:
        The core of the algorithm is to use a count matrix (which is of the same size as the m x n altitude
        values matrix) to memorize and update all the possible skiing paths from high altitudes to low altitudes.
        The algorithm sorts and considers altitudes from the altitude matrix from high to low. The count matrix will 
        start by containing '0's for all positions (meaning that no path has been created yet).
        Starting from the highest altitude (referred as the 'current position') in the altitude matrix (say 15), 
        consider all its 8 neighbors (down, up, left, right, and 4 diagonals). For neighbors with smaller 
        altitude values, update the count matrix values (referred as 'count values') of those neighbors' 
        positions by 1. This means that from the highest altitude (where 0 path
        can lead to that position), every neighboring altitude has 1 path leading 
        to it (therefore, their count values are all 1 now). We then proceed to the next highest altitude (say 13), 
        and check its neighbors again to record the positions of neighbors who have lower altitudes than the current 
        position, and update the neighbors' count values in the count matrix. Suppose the position of altitude 13 already 
        has a count value of 1 (it is 15's neighbor), now for 13's neighbors, they will have the count value of 1 + 1 = 2
        (inheriting 13's count value of 1 and add 1 to represent the new path.) We then proceed to the next 
        altitude values, until all positions in the altitude matrix have been explored. To be more specific, 
        if we encounter duplicate neighbors (that is, if there are two positions with the same altitude 12, 
        and they both have the neighbor altitude 11), we compare:
        (1)'count value for the current position + 1', 
        and
        (2)'the existing count values of the neighbors' positions' 
        and keep the larger value in the count matrix (if tie, keep either one). 
        If the 11 position already has a count value of 3, 
        and if its another neighbor wants to produce a count of 2 for it, we keep the value 3 
        (keeping the maximum number of paths possible). In this way, when we go through all the 
        altitude positions in the matrix and find the largest value in the count matrix, 
        we get the longest path possible. 

        To implement this algorithm, I created a sorted dictionary (again, like a priority queue), with 
        altitude values in descending order as keys, and matrix position(s) of the corresponding 
        altitude values as dictionary values (if there are multiple positions, append those to a list).
        I then go through all altitude values in descending order, and for the altitude's corresponding 
        matrix positions, I find their lower neighbors by looking for smaller altitude values in the 8 
        neighboring positions (I used 'if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])' to only keep 
        within-range neighbors). If a lower neighbor is found, I'll update that neighboring position's count 
        value in the count matrix (created seperately and all values start with 0), by keeping the larger 
        value between 'current position's count value + 1' and 'existing count value for that neighboring 
        position' using a max() function. In this way, after going through all positions in the altitude 
        matrix, we can find the longest path length by looking for the max value in the whole count matrix. 


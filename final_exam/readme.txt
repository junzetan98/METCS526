Question 1: 
    Input: 
        python question1_edit.py < flood_1 ~ 12.txt
    Output: 
        Screenshot Question_1 flood_Input 1-5
        Screenshot Question_1 flood_Input 6-10
        Screenshot Question_1 flood_Input 11-12
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
        Screenshot Question_2 ski_input 1-3
    Explanations:
        The core of the algorithm is to use a count matrix which 
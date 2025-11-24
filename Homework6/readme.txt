Problem1:
    Screenshots: Problem1_InsertionSort/MergeSort/QuickSort_Input_Small/Medium/large.png
    Inputs: python problem1_insertion/quick/merge.py < small/medium/large.txt
    (python generate_input_problem1.py is used to generate input files for problem 1 and 2)
    Explanation:
    (1) Insertion sort: the core of an insertion sort is to repeatedly compare values in different index positions, move greater-than-key values afterwards
        in the array, and insert the pivot key values back to the list.
    (2) Merge sort: the core of a merge sort is to divide the array down to sub-arrays containing 2 elements each, 
        then compare and sort the two elements in each sub-array, then compare each element in each sub-array and put the 
        smaller numbers to a new array for each comparison.
    (3) Quick sort: the core of a quick sort is to take the middle value (divide the length of array by 2) as pivot, and then 
        divide the array into three sequences: the left sequence contains elements that are smaller than the pivot value;
        the middle sequence contains elements that are equal to the pivot valuel the right sequence contains elements larger then the
        pivot value. Then, recurse this process on the left and right sequences until the lengths of sequences equal 1.

    For the inputs, the small input file contains 15 numbers, the medium input contains 50 numbers, and the large input contains 500 numbers.
    Based on my results, the quick sort performs best for large inputs (0.002 seconds), the merge sort performs best for medium inputs (0.0005 seconds),
    and the quick sort again performs best for small inputs (0.0003 seconds). The insertion sort works relatively well for small/medium inputs but not for 
    larger inputs (e.g. 500), probabaly because more computing power is needed when we need to repeatedly move each element in the array for each loop.
    The merge sort performs well for medium to large inputs but not so well for small inputs, probably because the process of dividing and merging does not
    improve efficiency for small inputs (when the length of array is small, it is quicker just to loop through all the elements than to reconstruct arrays).
    The quick sort performs well for arrays of all sizes, probably because it repeatly reduce the arrays' sizes during each recursion, making it
    efficient regardless of input sizes. 

    In summary, the quick sort should be the first choice when dealing with large inputs. For very small inputs (like 15 numbers), the insertion sort can be used.
    For inputs of size of about 50 numbers, the merge sort can be more useful.


Problem2:
    Screenshots: Problem2_RadixSort_Input_Small/Medium/Large.png
    Inputs: python problem2.py < small/medium/large.txt
    Explanation:
    The core of a radix sort is to compare each digit of the values in the array (not the actual values). The LSD (least significant digit) approach
    used here is to first compare the ones digit, then tens/hundreds digits, etc. The algorithm first finds out the maximum number in the array and 
    decides the number of digits we need to compare (e.g. if the maximum is 999, then the number of digits needed is 3). Then, the numbers in each digit place are
    compared and the relative orders are kept for each round of comparison, until all digit places have been compared and sorted.

    Radix sort performs well for large input arrays where the ranges of numbers in the arrays are big. It works well because it does not
    have to compare the actual numbers but only need to compare numbers from 0 to 9 for each digit place, making it efficient to compare numbers
    in large arrays. 


Problem3:
    Screenshots: Problem3_input_ten/hundred/thousand.png
    Inputs: 
        python problem3_copy.py < marriage_ten.txt
        python problem3_copy.py < marriage_hundred.txt
        python problem3_copy.py < marriage_thousand.txt
    Outputs Files:
        stable_matching_output_10.txt
        stable_matching_output_100.txt
        stable_matching_output_1000.txt
    Explanation:
        The core of the algorithm is the gale shapley algorithm. Specifically, the algorithm takes the input 
        file and read line index 1 (row 2) to index n+1 (row n+2) as the male list, and the remaining rows as the female list.
        The male and female lists contain males' and females' preferences which will be used for stable matching.
        During the stable matching process, the algorithm starts with the male list, takes the first man, and takes the 
        man's first prefered woman as his first proposal. At this point, three conditions can occur:
        (1) The proposed woman is not paired with any other man yet. In this case, the proposing man and proposed woman will become a 
            pair, and this pair information will be stored in a engaged list.
        (2) The proposed woman is already paired with another man. In this case, we need to consider the woman's preference. We retrieve the 
            woman's preference from the female list, and find the smaller index (because smaller index indicates priority and more preference in our case)
            between the new proposing man (idx_new) and the currently paired man (idx_current). In this case, there are two conditions:
                (a) if idx_new < idx_current, the woman prefers the new man more than the current man. In this case, the woman's pair will be 
                    updated to become the new man. For the current man, he will be put back to the male list for reconsideration (to implement this, 
                    an active man list will be created first to record which mans are not paired yet, and the preference of every man who already pairs with a woman will be stored in a maybe list
                    in case we need his information again when he is rejected by a women later in the process). 
                (b) if idx_new > idx_current, the woman prefers the current choice. In this case, the current pair will be kept, and the new
                    man will propose to his next preference in his preference list, until he finds a woman that makes him satisfy either condition(1) or condition(2-a) (to implement this, a while loop is used, and when a man reaches 
                    the current case, the index 1 of the current man's list will be poped so that the next woman's name can become the new index 1 in the new while loop).
        (3) If the man iterates through all his preferences but finds no match (an unlikely case), we will print out a warning message
            indicating that the pairing for this man fails.

        The above are the core logic of my algorithm. To accelerate the pairing process, once a man successfully pairs with a woman,
        the paired woman's name is deleted from the man's preference list (before storing the man's preference list to the backup list in case he needs to be paired again).
        This is because even when that man needs to re-pair, he will never need to consider again the woman who rejects him, as his ranking in that woman's preference
        can never be higher than the new man who the woman prefers more. This is done by poping the current woman's name once the man pairs with the woman.

        The implementation of this algorithm uses two while loops, where the first once loops through all the active mans and ends when there are no unengaged man left.
        The second loop iterates through a man's preference list (i.e. through the female names) and ends only if there is no more female in the preference list to propose to.



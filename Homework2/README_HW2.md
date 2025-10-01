# METCS526 HW2
To execute my codes results, please type in this in command line:
python HW2_Codes.py

Problem 1:
The tail pointer in a linked list is a pointer node that locates at the end of the current list
and points to the next linked list.　It effectively shows the 'end' of the current list. The advantage of using it is that when appending a new list to the existing linked list, the algorithm can quickly locate the end of the current list by looking at the tail pointer, without having to loop through all the elements of the existing list to find the last element of the linked list, therefore speeding up algorithm speed.

Problem 2:
The doIt function is a recursive function that calls on itself and prints a linked list in reversed order. The function moves to the next linked list value everytime being called and stops only when it reaches the end of the list. Then it prints the last value in the linked list first. That is why when I input a linked list with values 12, 3, 5, 2, the doIt function prints out 2, 5, 3, 12.

Problem 3:
The outputs:
doIt(1) = 1,
doIt(3) = 2,
doIt(6) = 4.

Problem 4: 
A doubly linked list is a linked list whose nodes have both a next pointer and a previous pointer. When trying to find the sum of three middle values in a doubly linked list, the two pointer method was used. This method makes a fast pointer moves twice as fast as a slow pointer. In this way, when the fast pointer moves a distance of n in the linked list, the slow pointer moves a distance of exactly n/2, which is the middle point of the linked list. Then, using the self.prev.value and self.next.value, we can find the middle three values of the doubly linked list. 


# Y1-Sem1-Lab9-CA

Exercises: For practice, do not use any inbuilt Python functions which we have not covered in class. Also make sure you use return 
and not print if something is to be returned from a function: 

1. Write a Python function to_english(n) that takes a positive or negative integer value ‘n’ and that returns a string containing 
the number expressed in English words.  
a. For example, if ‘n’ is 142, then the function should return the string “One hundred and forty two” (excluding the quotes). Note how the first word is capitalized. 
b. Think dictionary for comparison, string concat, division and modulus. 
c. Assume that ‘n’ is a value greater than -1000 and less than 1000 (so between -999 and 999).    
d. I will not be testing for values outside this range or for function parameters that are not integer. 
e. Examples: i. to_english(142) -> “One hundred and forty two” ii. to_english(-142) -> “Minus one hundred and forty two” iii. to_english(11) -> “Eleven" iv. to_english(42) 
-> “Forty two" v. to_english(9) -> “Nine" vi. to_english(999) -> “Nine hundred and ninety nine"   

2. Write a Python function sort_a_list(s) that takes a list of numbers or single characters 's' and returns a sorted list. 
a. You cannot use the python function sort(), but you can use min() and/or max() 
b. If the input parameter contains duplicate values, return a list containing only unique values (note: capital and lower case characters are not the same) 
c. Examples: 
    i. sort_a_list([2,-3]) -> [-3,2] 
    ii. sort_a_list([2,3,2]) -> [2,3] 
    iii. sort_a_list([2,3, 1]) -> [1,2,3] 
    iv. sort_a_list(['z','a']) -> ['a','z'] 
    v. sort_a_list(['H','B']) -> ['B', 'H'] 
    vi. sort_a_list(['a', 'B']) -> ['B','a'] 
    
 3. Write a Python function ascii_difference(m, n) which will take 2 lists 'm' and 'n' and will return two lists.  
 The first returned list is the combined ascii value of the elements @ the same index number, the second list is the absolute ascii 
 difference between each element @ the same index number: 
 a. ascii_difference([1, 2], [3, 4]) -> ([100, 102], [2, 2]) 
 b. ascii_difference(['a', 2], [3,4]) -> ([148, 102], [46, 2]) 
 c. ascii_difference([1,'b'], [3,4]) -> ([100, 150], [2, 46]) 
 d. ascii_difference(['1', '2', '3'], []) -> ([49, 50, 51], [49, 50, 51]) 
 e. ascii_difference([1,2], [3,'C']) -> ([100, 117], [2, 17]) 
 f. ascii_difference(['a','b'], ['z','d']) -> ([219, 198], [25, 2]) 

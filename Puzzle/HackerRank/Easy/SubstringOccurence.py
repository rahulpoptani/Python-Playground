'''
Find total number of occurrences of the substring in the original string. 
Input:
--------
ABCDCDC
CDC
Output:
--------
2
'''
def count_substring(string, sub_string):
    counter = 0
    for x in range(len(string)):
        if sub_string == string[x:x+len(sub_string)]:
            counter += 1
    return counter


    
count = count_substring('ABCDCDC', 'CDC')
print(count)
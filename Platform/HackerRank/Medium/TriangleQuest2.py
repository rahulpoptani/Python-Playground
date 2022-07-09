'''
Print a palindromic triangle of size N
You have to complete the code using exactly one print statement. 
Input:
-------
5
Output:
--------
1
121
12321
1234321
123454321
'''

for i in range(1,int(input())+1): # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((pow(10,i)-1)//9) * ((pow(10,i)-1)//9))
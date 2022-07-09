'''
Perform the follwing commands
insert i e: Insert integer e at position i
print: Print the list.
remove e: Delete the first occurrence of integer e
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Input:
-------
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Output:
--------
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    lst = []
    N = int(input())
    for _ in range(N):
        expression = input().split()
        command = expression[0]
        if command == 'print':
            print(lst)
        elif command == 'insert':
            lst.insert(int(expression[1]), int(expression[2]))
        elif command == 'append':
            lst.append(int(expression[1]))
        elif command == 'sort':
            lst = sorted(lst)
        elif command == 'reverse':
            lst.reverse()
        elif command == 'pop':
            lst = lst[0:len(lst)-1]
        elif command == 'remove':
            lst.remove(int(expression[1]))

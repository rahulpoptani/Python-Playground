my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
    # break If you call break then the else part will not be executed
else:       # Consider ELSE as NOBRAKE.
    print('This will run after the loop, only if "break" is not called')



# else will also work with While loop
i = 1
while(i < 5):
    print(i)
    i += 1
else:
    print('Else After While')


# Example Use Case
def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i

index_location = find_index(my_list, 4)
print('Location for target is: {}'.format(index_location))


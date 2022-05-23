my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# [start:end:step]


print('-----------------------------------')
print(my_list[3])
print(my_list[-3])

print('-----------------------------------')
print(my_list[1:9:2])
print(my_list[1:9:-2]) #nothing

print('-----------------------------------')
print(my_list[-3:])
print(my_list[3:-3])
print(my_list[-3:3]) #nothing
print(my_list[-3:3:-1]) #iterate backwards

print('-----------------------------------')
print(my_list[-9:-3])
print(my_list[1:8]) #both are same
print(my_list[:])

print('-----------------------------------')
print(my_list[::-1]) # leave start and end, just provide negative step
print(my_list[::1])


print('-----------------------------------')
sample_url = 'https://rahulpoptani.com'
print(sample_url[::-1])
print(sample_url[-4:])
print(sample_url[8:])
print(sample_url[8:-4])
def find_product(lst):
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    right = 1
    print(product)
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]
    return product

arr = [4,2,0,4,1]
print(arr)
print(find_product(arr))

# Time Complexity: Traverses the list twice, the time complexity is O(n)
